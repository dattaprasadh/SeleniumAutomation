import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary



def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
@pytest.fixture(scope="class")
def setup(request):
    browser_name=request.config.getoption("browser_name")
    if browser_name=="chrome":
        service_obj = Service(r"C:\Users\DHUDDAR\Documents\chrome\chromedriver")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name=="firefox":

        service_obj = Service(r"C:\Users\DHUDDAR\Downloads\geckodriver.exe")
        driver = webdriver.Firefox(firefox_binary=FirefoxBinary())

    request.cls.driver=driver
