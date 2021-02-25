import time
from PageObjects.CheckOutPage import CheckOutPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.DemoPage import DemoPage
from PageObjects.FlightFarePage import FlightFarePage
from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestYatra(BaseClass, DemoPage):
    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        self.driver.implicitly_wait(15)

        homePage.getFromLocation().click()
        time.sleep(1)
        homePage.getFromLocation().send_keys("BLR")
        time.sleep(2)
        homePage.getFromLocation().send_keys(Keys.ENTER)
        log.info("Entering from location")

        to_City = homePage.getToLocation()
        time.sleep(2)
        to_City.send_keys("PAT")
        time.sleep(3)
        to_City.send_keys(Keys.ENTER)
        log.info("Entering departure location")

        homePage.getOriginDate().click()
        homePage.getSelectdate().click()
        flightFarePage = homePage.getSearchButton()
        flightFarePage.getSortHighestPrice().click()
        checkOutPage = flightFarePage.getBookNowButton()
        time.sleep(10)
        checkOutPage.getEnter_Emailid("testing9934@gmail.com")
        checkOutPage.get_Mobile_No("9870466369")

        self.selectMrDropdown("Mr")

        checkOutPage.getFirstName("NeerajK")
        checkOutPage.getLastName("Singh")
        scrolldown_page = checkOutPage.getScrollDownHtml()
        scrolldown_page.send_keys(Keys.END)
        payment_button = WebDriverWait(self.driver, 10)
        payment_button.until(expected_conditions.presence_of_element_located(
           (By.XPATH, "//button[contains(text(),'Proceed To Payment')]")))
        time.sleep(5)
        checkOutPage.getProceedToPayment()
        paymentGateway = checkOutPage.getRiskMyTravelButton()
        paymentGateway.getAmazonPayment().click()
        paymentGateway.getAmazonPayment().click()


