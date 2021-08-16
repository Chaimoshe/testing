import pytest
import time
import json
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager


class TestTargil1():
    def setup_method(self):
        print('initiating web-driver')
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def teardown_method(self):
        self.driver.quit()

    def test_check_url(self):
        print('test_check_url')
        self.driver.get("https://1221.org.il/")
        # self.driver.set_window_size(1526, 833)
        URL = self.driver.current_url
        assert URL == "https://1221.org.il/"

    def test_check_title(self):
        print('test_check_title')
        expected_title = "רשת מתנדבים להצלת חיים\u200f - איחוד הצלה : איחוד הצלה"
        self.driver.get("https://1221.org.il/")
        title = self.driver.title
        print(f"title = {title}")
        print(f"expected_title = {expected_title}")
        assert title == expected_title
        # return title

    def test_check_move_page(self):
        print('test_check_move_page')
        self.driver.get("https://1221.org.il/")
        element = self.driver.find_element(By.LINK_TEXT, "תרומה 🧡")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.execute_script("arguments[0].click();", element)
        URL = self.driver.current_url
        assert URL == "https://1221.org.il/%d7%aa%d7%a8%d7%95%d7%9e%d7%94-%d7%a2%d7%91%d7%95%d7%a8-%d7%94%d7%a6%d7%9c%d7%aa-%d7%97%d7%99%d7%99%d7%9d/"



# iclass = TestTargil1()
# iclass.setup_method()
# iclass.test_check_url()
# iclass.test_check_title()
# iclass.test_check_move_page()
# iclass.teardown_method()
