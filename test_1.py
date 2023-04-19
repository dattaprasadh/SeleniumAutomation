from selenium import webdriver
from selenium.webdriver.chrome.service import Service
def test_method():
    service_obj = Service(r"C:\Users\DHUDDAR\Documents\chrome\chromedriver")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://www.google.com/")
