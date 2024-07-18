from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_display_empty_text(self):
        assert ((self.browser.find_element(*BasketPageLocators.EMPTY_TEXT)).text) == "Your basket is empty. Continue shopping", "No empty text"

    def should_be_no_items_in_the_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), "There is products in basket"