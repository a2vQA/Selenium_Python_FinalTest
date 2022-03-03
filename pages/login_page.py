from .locators import LoginPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.browser.find_element(By.ID, 'login_link').click()
        assert "/login" in self.browser.current_url, "current URL does not have 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.login_form), 'Login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.register_form), 'Register form is not presented'

    def register_new_user(self, email, password, browser):
        input1 = browser.find_element(By.CSS_SELECTOR, "#id_registration-email").send_keys(email)
        input2 = browser.find_element(By.CSS_SELECTOR, "#id_registration-password1").send_keys(password)
        input3 = browser.find_element(By.CSS_SELECTOR, "#id_registration-password2").send_keys(password)
        button_register = browser.find_element(By.CSS_SELECTOR, "#register_form .btn-primary").click()
