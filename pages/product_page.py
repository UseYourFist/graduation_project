from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    def add_to_basket(self):
        self.find_button_and_click()
    
    def find_button_and_click(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()

    def product_in_basket(self):
        assert ((self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)).text == (self.browser.find_element(*ProductPageLocators.NAME_IN_MESSAGE)).text) and ((self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)).text == (self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE)).text), 'not this product'

    def solve_quiz_and_get_code(self):
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