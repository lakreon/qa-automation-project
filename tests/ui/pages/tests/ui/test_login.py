import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def driver():
    service = Service()  # Авто-детект ChromeDriver
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.login("testuser@example.com", "testpass123")  # Используйте реальные creds для демо
    assert "Welcome" in login_page.is_logged_in()
