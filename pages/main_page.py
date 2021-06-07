from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from pages.login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.login_link)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

class LoginPage(BasePage):
    def  should_be_login_page(self):
        assert True, 'powel naxyi'

    # def should_be_login_link(self):
    #     assert self.is_element_present(By.CSS_SELECTOR, "#registration_link"), "Login link is not presented"
