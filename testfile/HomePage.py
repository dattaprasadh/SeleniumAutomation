from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver):
        self.driver=driver

    price=(By.XPATH,"(//span[@class='a-price-whole'])[1]")
    def getPrice(self):

       return self.driver.find_element(*HomePage.price)