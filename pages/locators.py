from selenium.webdriver.common.by import By


class MainPageLocators:
    login_link = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    login_form = (By.CSS_SELECTOR, "#login_form")
    register_form = (By.CSS_SELECTOR, "#register_form")


class BasketTaskLocators:
    basket_btn = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    added_name = (By.CSS_SELECTOR, '#messages>div:nth-child(1)>div>strong')
    book_name = (By.CSS_SELECTOR, '#content_inner>article>div.row>div.col-sm-6.product_main>h1')
    book_price = (By.CSS_SELECTOR, '#content_inner>article>div.row>div.col-sm-6.product_main>p.price_color')
    basket_price = (By.CSS_SELECTOR, '#messages>div.alert.alert-safe.alert-noicon.alert-info.fade.in>div>p:nth-child(1)>strong')
