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
    basket_price = (By.CSS_SELECTOR, '#messages>div.alert.alert-safe.alert-noicon.alert-info.fade.in>div>p:nth-child('
                                     '1)>strong')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    SUCCESS_MESSAGE1 = (By.CSS_SELECTOR, "#messages div.alertinner")


class AnyPageLocators:
    BASKET_BTN = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs > span > a")


class ProductPageLocators:
    button_basket = (By.CSS_SELECTOR, ".product_main .btn-add-to-basket")
    basket_message_sl = (By.CSS_SELECTOR, "#messages>:nth-child(1) strong")
    name_book = (By.CSS_SELECTOR, ".product_main h1")
    price_message = (By.CSS_SELECTOR, "#messages>:nth-child(3) strong")
    price = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div.alertinner")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    REGISTRY_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    PASSWORD_VERIFY = (By.CSS_SELECTOR, '#id_registration-password2')
