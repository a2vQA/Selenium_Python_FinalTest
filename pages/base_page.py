from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import math


class BasePage:
    def __init__(self, browser: webdriver, url):
        self.browser = browser
        self.url = url

    def __init__(self, browser, url, timeout=3):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, find_elements, login_link):
        try:
            self.browser.find_element(find_elements, login_link)
        except (NoSuchElementException):
            return False
        return True

    def open(self):
        self.browser.get(self.url)
