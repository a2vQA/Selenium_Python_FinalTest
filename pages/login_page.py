from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.find_element(By.ID, 'login_link').click()
        assert "/login" in self.browser.current_url, "current URL does not have 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.login_form1), 'Login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.register_form), 'Register form is not presented'
