from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from pages.login_page import LoginPage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)