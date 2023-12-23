from .base_page import BasePage
from .locators import LoginPageLocators
import time
from .helpers import *



class LoginPage(BasePage):

    @o
    def is_login_page(self):
        self.is_login_url()
        self.have_login_form()
        self.have_register_form()

    @o
    def is_login_url(self):
        assert 'login' in self.browser.current_url

    @o
    def have_login_form(self):
        assert self.is_element_present(LoginPageLocators.LOGIN_FORM)

    @o
    def have_register_form(self):
        assert self.is_element_present(LoginPageLocators.REGISTER_FORM)

    @o
    def register_new_user(self):
        email = str(time.time()) + '@fakemail.org'
        password = 'hfgfgFKFjdHfnY89798798'
        self.browser.find_element(*LoginPageLocators.EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASS1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASS2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_SUBMIT).click()
        