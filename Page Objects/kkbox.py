# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest, time

#創建一個引用 unittest 的測試用例
class KKBOXTestCase(unittest.TestCase):
    #測試前準備環境的搭建
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://play.kkbox.com")
        # login
        self.driver.find_element_by_id("uid").send_keys("mandyyang@kkbox.com")
        self.driver.find_element_by_id("pwd").send_keys("P299kkbox")
        self.driver.find_element_by_id("login-btn").send_keys(Keys.ENTER)
        time.sleep(2)
    #測試後環境的還原
    def tearDown(self):
        self.driver.close() 


    def test_search_artist(self):
        #搜尋歌手:韋禮安
        driver = self.driver
        driver.find_element_by_css_selector(".search_hint").send_keys(u"韋禮安")
        time.sleep(1)
        driver.find_element_by_css_selector(".search_hint").send_keys(Keys.ENTER)
        time.sleep(2)
        search_results = driver.find_elements_by_css_selector("ul.cards.artists")
        time.sleep(1)
        for search_result in search_results:
            self.assertIn(u"韋禮安", search_result.text)


    def test_search_song(self):
        #搜尋歌曲:因為愛
        driver = self.driver
        driver.find_element_by_css_selector(".search_hint").send_keys(u"因為愛")
        time.sleep(1)
        driver.find_element_by_css_selector(".search_hint").send_keys(Keys.ENTER)
        time.sleep(2)
        # 取得 song table, 每一列（tr:橫向）
        song_table = driver.find_elements_by_css_selector(".songs-table tr")
        # 第一列是項目名稱, 不需要, 所以只取第二列到最後一列 [1:]
        for row in song_table[1:]:
            # 取得第二欄（td:直向）, 歌曲名稱
            search_result = row.find_elements_by_tag_name("td")[1]
            self.assertIn(u"因為愛", search_result.text)


    def test_search_song_list(self):
        #搜尋歌單:韋禮安 (William Wei) 歷年精選
        driver = self.driver
        driver.find_element_by_css_selector(".search_hint").send_keys(u"韋禮安 (William Wei) 歷年精選")
        time.sleep(1)
        driver.find_element_by_css_selector(".search_hint").send_keys(Keys.ENTER)
        time.sleep(2)
        search_results = driver.find_elements_by_css_selector("ol.cards")
        time.sleep(1)
        for search_result in search_results:
            self.assertIn(u"韋禮安 (William Wei) 歷年精選", search_result.text)


#測試執行
if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [KKBOXTestCase("test_search_artist"), 
             KKBOXTestCase("test_search_song"), 
             KKBOXTestCase("test_search_song_list")]

    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)