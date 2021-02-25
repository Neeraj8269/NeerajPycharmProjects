from selenium.webdriver.common.by import By
from PageObjects.CheckOutPage import CheckOutPage


class FlightFarePage:
    def __init__(self, driver):
        self.driver = driver

    sortHighestPrice = (By.CSS_SELECTOR, "p[class*='link-color bold']")
    BookNow_Button = (By.XPATH, "//div[@class='result-set pr grid']/div/div[1]/div/div/div[4]/div/div[2]/button")

    def getSortHighestPrice(self):
        return self.driver.find_element(*FlightFarePage.sortHighestPrice)

    def getBookNowButton(self):
        self.driver.find_element(*FlightFarePage.BookNow_Button).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

