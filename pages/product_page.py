import math
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from selenium import webdriver
from .base_page import BasePage
from .locators import BasketTaskLocators, ProductPageLocators


class ProductPage(BasePage):

    def popup_alert(self):
        browser = webdriver
        btn = self.browser.find_element(*BasketTaskLocators.basket_btn).click()

    def check_message_about_adding_to_basket(self):
        basket_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def check_success_message_on_product_page(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def solve_quiz_and_get_code(self):
        WebDriverWait(self.browser, 3).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def name_check(self):
        added_name = self.browser.find_element(*BasketTaskLocators.added_name).text
        book_name = self.browser.find_element(*BasketTaskLocators.book_name).text
        assert book_name == added_name, "books are different"

    def price_check(self):
        book_price = self.browser.find_element(*BasketTaskLocators.book_price).text
        basket_price = self.browser.find_element(*BasketTaskLocators.basket_price).text
        assert book_price == basket_price, "price are different"
