from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert LoginPageLocators.LOGIN_URL in self.browser.current_url, 'not the authorization page'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'no authorization form'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), 'no reg form'

    def register_new_user(self, email, password):
        login = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        login.send_keys(email)
        pass1 = self.browser.find_element(*LoginPageLocators.REG_PASS1)
        pass1.send_keys(password)
        pass2 = self.browser.find_element(*LoginPageLocators.REG_PASS2)
        pass2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REG_FORM)
        button.click()