import json
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_user_login(driver):
    with open("data/login_data.json") as f:
        data = json.load(f)

    driver.get("https://example.com/login")

    driver.find_element(By.ID, "email").send_keys(data["email"])
    driver.find_element(By.ID, "password").send_keys(data["password"])
    driver.find_element(By.ID, "loginBtn").click()

    assert "dashboard" in driver.current_url

    os.makedirs("screenshots", exist_ok=True)
    driver.save_screenshot("screenshots/login_success.png")
