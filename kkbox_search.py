# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest, time

class KKBOXTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://play.kkbox.com")
        # login
        self.driver.find_element_by_id("uid").send_keys("mandyyang@kkbox.com")
        self.driver.find_element_by_id("pwd").send_keys("P299kkbox")
        self.driver.find_element_by_id("login-btn").send_keys(Keys.ENTER)
        time.sleep(2)

    def test_search_artist(self):
    	driver = self.driver
        driver.find_element_by_tag_name("input").send_keys(u"韋禮安")
        time.sleep(1)
        driver.find_element_by_tag_name("input").send_keys(Keys.ENTER)
        time.sleep(1)
        searchResult = driver.find_element_by_link_text(u"韋禮安 (William Wei)").text
        assert u"韋禮安 (William Wei)" in searchResult

    def test_search_song(self):
        driver = self.driver
        driver.find_element_by_tag_name("input").send_keys(u"因為愛")
        time.sleep(1)
        driver.find_element_by_tag_name("input").send_keys(Keys.ENTER)
        time.sleep(1)
        searchResult = driver.find_element_by_link_text(u"因為愛").text
        assert u"因為愛" in searchResult    	

    def test_search_playlist(self):
        driver = self.driver
        driver.find_element_by_tag_name("input").send_keys(u"有人在等")
        time.sleep(1)
        driver.find_element_by_tag_name("input").send_keys(Keys.ENTER)
        time.sleep(1)
        searchResult = driver.find_element_by_link_text(u"有人在等").text
        assert u"有人在等" in searchResult 


if __name__ == "__main__":
    unittest.main()