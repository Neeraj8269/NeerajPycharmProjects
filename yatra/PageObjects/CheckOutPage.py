from selenium.webdriver.common.by import By

from PageObjects.PaymentGateway import PaymentGateway


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    enter_Email = (By.ID, "additionalContactEmail")
    enter_MobileNo = (By.ID, "additionalContactMobile")
    selectDropdownTitle = (By.NAME, "title0")
    FirstName = (By.NAME, "fname0")
    LastName = (By.NAME, "lname0")
    ScrolldownHtml = (By.TAG_NAME, "html")
    proceedToPayment = (By.XPATH, "//button[contains(text(),'Proceed To Payment')]")
    riskMyTravelButton = (By.CSS_SELECTOR, "input[value='Risk My Travel']")

    def getEnter_Emailid(self):
        return self.driver.find_element(*CheckOutPage.enter_Email)

    def get_Mobile_No(self):
        return self.driver.find_element(*CheckOutPage.enter_MobileNo)

    def getDropdownTitle(self):
        return self.driver.find_element(*CheckOutPage.selectDropdownTitle)

    def getFirstName(self):
        return self.driver.find_element(*CheckOutPage.FirstName)

    def getLastName(self):
        return self.driver.find_element(*CheckOutPage.LastName)

    def getScrollDownHtml(self):
        return self.driver.find_element(*CheckOutPage.ScrolldownHtml)

    def getProceedToPayment(self):
        return self.driver.find_element(*CheckOutPage.proceedToPayment).click()

    def getRiskMyTravelButton(self):
        self.driver.find_element(*CheckOutPage.riskMyTravelButton).click()
        paymentGateway = PaymentGateway(self.driver)
        return paymentGateway

