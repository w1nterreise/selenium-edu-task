from selenium.webdriver.common.by import By




class Uri():

    MAIN = "http://selenium1py.pythonanywhere.com/en-gb/"
    LOGIN = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    PRODUCT = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/metasploit_193/"


class BasePageLocators():

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    CART_BUTTON = (By.XPATH, "//*[@id='default']/header/div[1]/div/div[2]/span/a")
    LANGUAGE = (By.NAME, 'language')
    LANGUAGE_APPLY = (By.XPATH, '//*[@id="language_selector"]/button')


class LoginPageLocators():

    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")   
    EMAIL = (By.ID, "id_registration-email")
    PASS1 = (By.ID, "id_registration-password1")
    PASS2 = (By.ID, "id_registration-password2")
    REG_SUBMIT = (By.NAME, "registration_submit")


class ProductPageLocators():

    PRODUCT_TITLE = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    ADDED_TITLE = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    ADDED_PRICE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    ADD_TO_CART = (By.CSS_SELECTOR, '.btn-add-to-basket')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner')   


class CartPageLocators():

    BASKET_EMPTY = (By.XPATH, '//*[@id="content_inner"]/p')
    BASKET_CONTENTS = (By.XPATH, '//*[@id="content_inner"]/div[1]')
    
    
class Locale():

    empty_cart = {
        'ar'    : 'سلة التسوق فارغة',
        'ca'    : 'La seva cistella està buida',
        'cs'    : 'Váš košík je prázdný',
        'da'    : 'Din indkøbskurv er tom',
        'de'    : 'Ihr Warenkorb ist leer',
        'en-gb' : 'Your basket is empty',
        'el'    : 'Το καλάθι σας είναι άδειο',
        'es'    : 'Tu carrito esta vacío',
        'fi'    : 'Korisi on tyhjä',
        'fr'    : 'Votre panier est vide',
        'it'    : 'Il tuo carrello è vuoto',
        'ko'    : '장바구니가 비었습니다',
        'nl'    : 'Je winkelmand is leeg',
        'pl'    : 'Twój koszyk jest pusty',
        'pt'    : 'O carrinho está vazio',
        'pt-br' : 'Sua cesta está vazia',
        'ro'    : 'Cosul tau este gol',
        'ru'    : 'Ваша корзина пуста',
        'sk'    : 'Váš košík je prázdny',
        'uk'    : 'Ваш кошик пустий',
        'zh-cn' : 'Your basket is empty'       
        }