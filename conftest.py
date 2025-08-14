# conftest.py
import json
import os
from pathlib import Path
import pytest

# ----- Configuration loading -----
DEFAULT_CONFIG_PATH = Path(__file__).resolve().parent / "config" / "api_test_configuration.json"

def load_config(path: str | None = None) -> dict:
    cfg_path = Path(path).resolve() if path else DEFAULT_CONFIG_PATH
    if not cfg_path.exists():
        # Fallback to a basic config if the file doesn't exist
        return {
            "api_base_url": "https://httpbin.org",
            "test_mode": "api",
            "headless": True,
            "window_size": "1920,1080",
            "implicit_wait_secs": 5,
            "explicit_wait_secs": 10
        }
    with cfg_path.open("r", encoding="utf-8") as f:
        return json.load(f)

# ----- CLI options -----
def pytest_addoption(parser: pytest.Parser) -> None:
    group = parser.getgroup("qa")
    group.addoption(
        "--config",
        action="store",
        dest="config_path",
        default=None,
        help="Path to config JSON file (defaults to ./config/api_test_configuration.json)",
    )
    group.addoption(
        "--mode",
        action="store",
        dest="override_mode",
        default=None,
        choices=["api", "ui"],
        help="Override test_mode from config (api|ui)",
    )

# ----- Fixtures -----
@pytest.fixture(scope="session")
def config(request: pytest.FixtureRequest) -> dict:
    cfg_path = request.config.getoption("config_path")
    cfg = load_config(cfg_path)
    override_mode = request.config.getoption("override_mode") or os.environ.get("TEST_MODE")
    if override_mode:
        cfg["test_mode"] = str(override_mode).lower()
    return cfg

@pytest.fixture(scope="session")
def is_ui(config: dict) -> bool:
    return str(config.get("test_mode", "api")).lower() == "ui"

@pytest.fixture(scope="session")
def driver(config: dict, is_ui: bool):
    if not is_ui:
        # In API mode, no browser is started; UI tests will be skipped in their fixtures/tests.
        yield None
        return

    # Lazy import so API-only runs don't require selenium
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    import os

    options = Options()
    if config.get("headless", True):
        # --headless=new is recommended for modern Chrome
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")

    size = config.get("window_size")
    if size:
        options.add_argument(f"--window-size={size}")

    # Try to find ChromeDriver in common locations
    chromedriver_paths = [
        os.path.join(os.environ.get('LOCALAPPDATA', ''), 'Programs', 'Python', 'Python313', 'chromedriver.exe'),
        os.path.join(os.environ.get('PROGRAMFILES', ''), 'Google', 'Chrome', 'Application', 'chromedriver.exe'),
        'chromedriver.exe'  # Fallback to PATH
    ]
    
    chromedriver_path = None
    for path in chromedriver_paths:
        if os.path.exists(path):
            chromedriver_path = path
            break
    
    if chromedriver_path:
        service = Service(executable_path=chromedriver_path)
        drv = webdriver.Chrome(service=service, options=options)
    else:
        # Fallback to Selenium Manager if ChromeDriver not found
        drv = webdriver.Chrome(options=options)
    imp_wait = int(config.get("implicit_wait_secs", 0))
    if imp_wait:
        drv.implicitly_wait(imp_wait)

    try:
        yield drv
    finally:
        drv.quit()

@pytest.fixture
def actions(driver, config: dict):
    if driver is None:
        pytest.skip("UI actions requested but test is running in API mode")
    # Lazy import for API-only runs
    from config.selenium_action_utils import SeleniumActions
    return SeleniumActions(driver, wait_seconds=int(config.get("explicit_wait_secs", 10)))

# ----- Markers and dynamic skipping -----
def pytest_configure(config: pytest.Config) -> None:
    config.addinivalue_line("markers", "api: mark test as API test")
    config.addinivalue_line("markers", "ui: mark test as UI test")

def pytest_runtest_setup(item: pytest.Item) -> None:
    # Resolve mode for current run
    override = item.config.getoption("override_mode")
    cfg_path = item.config.getoption("config_path")
    mode = (override or load_config(cfg_path).get("test_mode", "api")).lower()

    is_ui_test = any(mark.name == "ui" for mark in item.iter_markers())
    is_api_test = any(mark.name == "api" for mark in item.iter_markers())

    if mode == "api" and is_ui_test:
        pytest.skip("Skipping UI test in API mode")
    if mode == "ui" and is_api_test:
        pytest.skip("Skipping API test in UI mode")
