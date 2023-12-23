from .base_page import BasePage
from .locators import CartPageLocators
from .locators import Locale
from .helpers import *



class CartPage(BasePage):

    @o
    def is_cart_page(self):
        assert 'basket' in self.browser.current_url

    @o
    def no_goods_in_cart(self):
        assert self.is_not_element_present(CartPageLocators.BASKET_CONTENTS)

    @o
    def has_text_about_no_goods(self):
        lang = self.browser.current_url.split('/')[-3]
        elem = self.browser.find_element(*CartPageLocators.BASKET_EMPTY)
        assert Locale.empty_cart[lang] in elem.text