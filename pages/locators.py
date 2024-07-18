from selenium.webdriver.common.by import By

class MainPageLocators:
    pass

class LoginPageLocators:
    LOGIN_FORM = (By.NAME, 'login_submit')
    REG_FORM = (By.NAME, 'registration_submit')
    LOGIN_URL = 'login'
    REG_EMAIL = (By.NAME, 'registration-email')
    REG_PASS1 = (By.NAME, 'registration-password1')
    REG_PASS2 = (By.NAME, 'registration-password2')

class ProductPageLocators:
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".basket-title.hidden-xs")