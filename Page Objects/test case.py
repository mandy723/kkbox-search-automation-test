# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest, time
import page

class KKBOXSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://play.kkbox.com")
        login_page = page.LoginPage(self.driver)
        login_page.id_text_element = "xxxxxxx@gmail.com"
        login_page.password_text_element = "xxxxxxxx"
        login_page.click_go_button()

    def tearDown(self):
        self.driver.close()

    def test_search_artist(self):
        """
        Tests python.org search feature. Searches for the word "pycon" then verified that some results show up.
        Note that it does not look for any particular text in search results page. This test verifies that
        the results were not empty.
        """

        #Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        #Checks if the word "Python" is in title
        assert main_page.is_title_matches(), "kkbox title doesn't match."
        #Sets the text of search textbox to "pycon"
        main_page.search_text_element = u"韋禮安"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        #Verifies that the results page is not empty
        assert search_results_page.is_results_found(), "No results found."



if __name__ == "__main__":
    unittest.main()