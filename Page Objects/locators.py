# -*- coding: UTF-8 -*-

from selenium.webdriver.common.by import By

class BasePageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    Login_BUTTON = (By.ID, 'login-btn')

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.ID, 'search_btn_cnt')

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass
