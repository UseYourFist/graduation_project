from selenium.webdriver.common.by import By

class ProductPageLocators:
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, ".alertinner p strong")