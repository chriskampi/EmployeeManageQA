from typing import Optional, List
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumActions:
    def __init__(self, driver: WebDriver, wait_seconds: int = 10):
        self.driver = driver
        self.wait_seconds = wait_seconds

    def open_url(self, url: str) -> None:
        self.driver.get(url)

    def wait_visible(self, by: By, locator: str, timeout: Optional[int] = None) -> WebElement:
        w = WebDriverWait(self.driver, timeout or self.wait_seconds)
        return w.until(EC.visibility_of_element_located((by, locator)))

    def click(self, by: By, locator: str, timeout: Optional[int] = None) -> None:
        el = self.wait_visible(by, locator, timeout)
        el.click()

    def type(self, by: By, locator: str, text: str, clear: bool = True, timeout: Optional[int] = None) -> None:
        el = self.wait_visible(by, locator, timeout)
        if clear:
            el.clear()
        el.send_keys(text)

    def get_text(self, by: By, locator: str, timeout: Optional[int] = None) -> str:
        el = self.wait_visible(by, locator, timeout)
        return el.text

    def find(self, by: By, locator: str) -> WebElement:
        return self.driver.find_element(by, locator)

    def finds(self, by: By, locator: str) -> List[WebElement]:
        return self.driver.find_elements(by, locator)
