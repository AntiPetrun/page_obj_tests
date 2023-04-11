from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, browser, url, email, password):
        super().__init__(browser, url)
        self.email = email
        self.password = password

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        expected_url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        current_url = self.browser.current_url
        assert expected_url == current_url, "Current url doesn't match with expected url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Register form not found"

    def register_new_user(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL).send_keys(self.email)
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys(self.password)
        self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM).send_keys(self.password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION).click()
