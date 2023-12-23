import math
import selenium.common.exceptions as SCE
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from selenium.webdriver.support.ui import Select
import random
from .helpers import *

    
    

class BasePage():

    def __init__(self, browser, uri=None, timeout=4):
        self.browser = browser
        self.uri = browser.current_url if uri is None else uri
        self.browser.implicitly_wait(timeout)
    
    @o
    def open(self):
        self.browser.get(self.uri)
    
    @o
    def go_to_login_page(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
    
    @o
    def go_to_cart_page(self):
        self.browser.find_element(*BasePageLocators.CART_BUTTON).click()
    
    @o
    def set_random_language(self):
        select = Select(self.browser.find_element(*BasePageLocators.LANGUAGE))
        select.select_by_index(random.randint(0, len(select.options) - 1))
        self.browser.find_element(*BasePageLocators.LANGUAGE_APPLY).click()
    
    @o
    def is_authorized_user(self):
        assert self.is_element_present(BasePageLocators.USER_ICON)
               
    @o
    def has_login_link(self):
        assert self.is_element_present(BasePageLocators.LOGIN_LINK)
    
    
    
    
    @catch(SCE.NoSuchElementException, False)
    def is_element_present(self, elem):
        self.browser.find_element(*elem)
    
    
    @catch(SCE.TimeoutException, True)
    def is_not_element_present(self, elem, timeout=4):
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(elem))
    
    
    @catch(SCE.TimeoutException, False)
    def is_disappeared(self, elem, timeout=4):
        WebDriverWait(self.browser, timeout, 1, SCE.TimeoutException).until_not(EC.presence_of_element_located(elem))
    

    

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")