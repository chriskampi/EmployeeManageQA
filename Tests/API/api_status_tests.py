import pytest
import requests

pytestmark = pytest.mark.api

def test_get_status_ok(config: dict):
    base = config.get("api_base_url", "https://httpbin.org")
    r = requests.get(f"{base}/status/200", timeout=10)
    assert r.status_code == 200

def test_json_echo(config: dict):
    base = config.get("api_base_url", "https://httpbin.org")
    payload = {"hello": "world"}
    r = requests.post(f"{base}/anything", json=payload, timeout=10)
    r.raise_for_status()
    data = r.json()
    assert data["json"] == payload
