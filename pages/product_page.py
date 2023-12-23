from .locators import ProductPageLocators
from .base_page import BasePage
from .helpers import *




class ProductPage(BasePage):

    @o
    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART).click()

    @o
    def title_is_correct(self):
        title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        title_message = self.browser.find_element(*ProductPageLocators.ADDED_TITLE).text
        assert title == title_message

    @o
    def price_is_correct(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_message = self.browser.find_element(*ProductPageLocators.ADDED_PRICE).text
        assert price == price_message

    @o
    def was_success_message(self):
        assert self.is_element_present(ProductPageLocators.SUCCESS_MESSAGE)

    @o
    def have_no_success_message(self):
        assert self.is_not_element_present(ProductPageLocators.SUCCESS_MESSAGE)

    @o
    def success_message_should_disappeared(self):
        assert self.is_disappeared(ProductPageLocators.SUCCESS_MESSAGE)
