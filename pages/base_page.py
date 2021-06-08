from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import math
from .locators import BasePageLocators
from .locators import AnyPageLocators


class BasePage:
    def __init__(self, browser: webdriver, url):
        self.browser = browser
        self.url = url

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def forward_to_basket(self):
        to_basket = self.browser.find_element(*AnyPageLocators.BASKET_BTN).click()

    def go_to_login_page_F(self):
        login = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID).click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def open(self):
        self.browser.get(self.url)

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
