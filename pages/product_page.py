from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
import math
from selenium import webdriver
# from .locators import BasketTaskLocators

class ProductPage(BasePage):

    def popup_alert(self):
        browser = webdriver
        btn = self.browser.find_element_by_css_selector('.btn.btn-lg.btn-primary.btn-add-to-basket').click()

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
        added_name = self.browser.find_element_by_css_selector('#messages>div:nth-child(1)>div>strong').text
        book_name = self.browser.find_element_by_css_selector('#content_inner>article>div.row>div.col-sm-6'
                                                              '.product_main>h1').text
        assert book_name == added_name, "books are different"

    def price_check(self):
        book_price = self.browser.find_element_by_css_selector('#content_inner>article>div.row>div.col-sm-6.product_main>p.price_color').text
        basket_price = self.browser.find_element_by_css_selector('#messages>div.alert.alert-safe.alert-noicon.alert-info.fade.in>div>p:nth-child(1)>strong').text
        assert book_price == basket_price, "price are different"
