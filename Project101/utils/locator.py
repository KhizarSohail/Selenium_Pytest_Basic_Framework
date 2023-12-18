from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    USERNAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN = (By.ID, 'login-button')
    ERROR_MESSAGE = (By.CLASS_NAME, 'product_label')
