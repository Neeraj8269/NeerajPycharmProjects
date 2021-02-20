from selenium.webdriver.common.by import By

from PageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitles = (By.XPATH, "//div[@class='card h-100']")
    checkOutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    finalCheckOut = (By.CSS_SELECTOR, "button[class*='btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitles)

    def getCheckOutButton(self):
        return self.driver.find_element(*CheckOutPage.checkOutButton)

    def getFinalCheckout(self):
        self.driver.find_element(*CheckOutPage.finalCheckOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage





















