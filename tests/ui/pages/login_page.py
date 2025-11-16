from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.demoblaze.com/index.html"
        self.login_btn = (By.ID, "login2")
        self.username = (By.ID, "loginusername")
        self.password = (By.ID, "loginpassword")
        self.submit_btn = (By.XPATH, "//button[text()='Log in']")
        self.welcome_text = (By.XPATH, "//p[contains(text(), 'Welcome') or contains(text(), 'PRODUCT STORE')]")

    def open(self):
        self.driver.get(self.url)

    def click_login(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_btn)).click()

    def enter_username(self, username):
        self.driver.find_element(*self.username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def submit_login(self):
        self.driver.find_element(*self.submit_btn).click()

    def login(self, username, password):
        self.click_login()
        self.enter_username(username)
        self.enter_password(password)
        self.submit_login()

    def is_logged_in(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.welcome_text)).text
