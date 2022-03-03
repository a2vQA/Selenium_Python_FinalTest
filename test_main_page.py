import time
import pytest
from .pages.login_page import LoginPage


@pytest.mark.login_guest
class TestLoginFromPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_link()
        page.should_be_login_page()
        page.go_to_login_page()
        login_page = page.go_to_login_page()
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/"
        page = LoginPage(browser, link)
        page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    browser.get(link)
    browser.find_element_by_css_selector('div.basket-mini.pull-right.hidden-xs > span > a').click()
    time.sleep(2)
    # assert browser.find_element_by_css_selector('.total align-right') == 0, "basket not empty"
    assert browser.find_element_by_css_selector('#content_inner > p').text == "Ваша корзина пуста Продолжить покупки", \
        "message of " \
        "empty basket " \
        "is presented "
