import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
import pages.locators as PL




@pytest.mark.guest
class TestLoginFromMainPage():

    def test_guest_should_see_login_link(self, browser):
        MainPage(browser, PL.Uri.MAIN).open().has_login_link()


    def test_guest_can_go_to_login_page(self, browser):
        MainPage(browser, PL.Uri.MAIN).open().go_to_login_page()
        LoginPage(browser).is_login_page()




class TestCartFromMainPage():

    def test_guest_see_no_product_in_cart_opened_from_main_page(self, browser):
        MainPage(browser, PL.Uri.MAIN).open().go_to_cart_page()
        CartPage(browser).is_cart_page().no_goods_in_cart().has_text_about_no_goods()


    @pytest.mark.locale    
    def test_empty_cart_locale(self, browser):
        MainPage(browser, PL.Uri.MAIN).open().set_random_language().go_to_cart_page()
        CartPage(browser).has_text_about_no_goods()
       
        