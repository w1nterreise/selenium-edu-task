import pytest
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
import pages.locators as PL




def can_add_goods_to_cart(browser):
    ProductPage(browser, PL.Uri.PRODUCT).open().add_to_cart().title_is_correct().price_is_correct()


@pytest.mark.user
class TestUserAddToCartFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        LoginPage(browser, PL.Uri.LOGIN).open().register_new_user()


    def test_user_cant_see_success_message(self, browser):
        ProductPage(browser, PL.Uri.PRODUCT).open().have_no_success_message()


    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        can_add_goods_to_cart(browser)
        


@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
    can_add_goods_to_cart(browser)


@pytest.mark.need_review
def test_guest_see_no_product_in_cart_opened_from_product_page(browser):
    ProductPage(browser, PL.Uri.PRODUCT).open().go_to_cart_page()
    CartPage(browser, browser.current_url).no_goods_in_cart().has_text_about_no_goods()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    ProductPage(browser, PL.Uri.PRODUCT).open().go_to_login_page()
    LoginPage(browser, browser.current_url).is_login_page()


@pytest.mark.xfail(reason='this test should fail')
def test_message_disappeared_after_adding_product_to_cart(browser):
    ProductPage(browser, PL.Uri.PRODUCT).open().add_to_cart().success_message_should_disappeared()