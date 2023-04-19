import time
from concurrent.futures import thread

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from testfile.HomePage import HomePage
from utilities.IndexClass import IndexClass


class TestOne(IndexClass):

    def test_e2e(self):
        homePage=HomePage(self.driver)
        self.driver.get("https://www.amazon.in/")
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR," input[id='twotabsearchtextbox']").send_keys("Mobile")
        time.sleep(4)
        self.driver.find_element(By.XPATH," // input[ @ id = 'nav-search-submit-button']").click()
        time.sleep(4)
        print(self.driver.find_element(By.XPATH, "//*[contains(text(),'Redmi 12C (Royal Blue, 4GB RAM, 64GB Storage)')]").text)
        print(homePage.getPrice().text)




