import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager

class TestUntitled():
  def setup_method(self):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_file_login(self):
    self.driver.get("https://school.1221.org.il/moodle/login/")
    self.driver.find_element(By.ID, "username").send_keys("5674ytu")
    self.driver.find_element(By.ID, "loginbtn").click()
    eror_message = self.driver.find_element(By.CSS_SELECTOR, ".alert").text
    assert eror_message == "שם משתמש או סיסמה שהזנתם אינם תקינים"

  def test_login(self):
    self.driver.get("https://school.1221.org.il/moodle/login/")
    self.driver.find_element(By.ID, "username").send_keys("302974183")
    self.driver.find_element(By.ID, "password").send_keys("12345678")
    self.driver.find_element(By.ID, "loginbtn").click()
    user_name = self.driver.find_element(By.CSS_SELECTOR, ".usertext").text
    assert user_name == "חיים משה רודניצקי"



iclass = TestUntitled()
iclass.setup_method()
iclass.test_file_login()
iclass.test_login()
iclass.teardown_method()
