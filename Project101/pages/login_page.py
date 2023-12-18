from utils.locator import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.locator = LoginPageLocators

    def wait_for_element(self, element):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(element)
        )

    def enter_username(self, username):
        self.wait_for_element(self.locator.USERNAME)
        self.driver.find_element(*self.locator.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.wait_for_element(self.locator.PASSWORD)
        self.driver.find_element(*self.locator.PASSWORD).send_keys(password)


    def click_login_button(self):
        self.wait_for_element(self.locator.LOGIN)
        self.driver.find_element(*self.locator.LOGIN).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def login_with_valid_user(self):
        self.login("standard_user", "secret_sauce")
        return LoginPage(self.driver)
