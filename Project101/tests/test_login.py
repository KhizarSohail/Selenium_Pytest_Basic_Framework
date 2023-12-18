from tests.base_test import BaseTest
from pages.login_page import LoginPage


class TestLogin(BaseTest):
    def test_login_with_valid_user(self):
        login_page = LoginPage(self.driver)

        login_page.login_with_valid_user()

        # self.assertIn("logged-in-successfully", self.driver.current_url)