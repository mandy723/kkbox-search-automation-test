# -*- coding: UTF-8 -*-

from element import BasePageElement
from element import LoginPageElement
from locators import MainPageLocators
from locators import BasePageLocators
import time

class IDTextElement(LoginPageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = 'uid'


class PasswordTextElement(LoginPageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = 'pwd'


class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = '.search_hint'


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):
    id_text_element = IDTextElement()
    password_text_element = PasswordTextElement()


    def click_go_button(self):
        element = self.driver.find_element(*BasePageLocators.Login_BUTTON)
        element.click()


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return "KKBOX" in self.driver.title

    def click_go_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        time.sleep(3)
        return u"韋禮安 (William Wei)" in self.driver.page_source