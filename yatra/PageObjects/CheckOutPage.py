from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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
    hotel_input_email = (By.ID, "additionalContactEmail")
    hotel_input_mobile = (By.ID, "additionalContactMobile")
    hotel_select_dropdown = (By.NAME, "title0")
    hotel_input_firstname = (By.NAME, "fname0")
    hotel_input_lastname = (By.NAME, "lname0")
    hotel_proceed_to_payment_button = (By.CSS_SELECTOR, "div[class*='sticky-sm-bottom'] button:nth-child(1)")

    def getEnter_Emailid(self, text):
        return self.driver.find_element(*CheckOutPage.enter_Email).send_keys(text)

    def get_Mobile_No(self, text):
        return self.driver.find_element(*CheckOutPage.enter_MobileNo).send_keys(text)

    def getDropdownTitle(self):
        return self.driver.find_element(*CheckOutPage.selectDropdownTitle)

    def getFirstName(self, text):
        return self.driver.find_element(*CheckOutPage.FirstName).send_keys(text)

    def getLastName(self, text):
        return self.driver.find_element(*CheckOutPage.LastName).send_keys(text)

    def getScrollDownHtml(self):
        return self.driver.find_element(*CheckOutPage.ScrolldownHtml)

    def getProceedToPayment(self):
        return self.driver.find_element(*CheckOutPage.proceedToPayment).click()

    def getRiskMyTravelButton(self):
        self.driver.find_element(*CheckOutPage.riskMyTravelButton).click()
        paymentGateway = PaymentGateway(self.driver)
        return paymentGateway

    def get_hotel_input_email(self):
        return self.driver.find_element(*CheckOutPage.hotel_input_email)

    def get_hotel_input_mobile(self):
        return self.driver.find_element(*CheckOutPage.hotel_input_mobile)

    def get_hotel_select_dropdown(self):
        return self.driver.find_element(*CheckOutPage.hotel_select_dropdown)

    def get_hotel_input_firstname(self):
        return self.driver.find_element(*CheckOutPage.hotel_input_firstname)

    def get_hotel_input_lastname(self):
        return self.driver.find_element(*CheckOutPage.hotel_input_lastname)

    def get_proceed_to_payment_button(self):
        self.driver.find_element(*CheckOutPage.hotel_proceed_to_payment_button).click()
        paymentGateway = PaymentGateway(self.driver)
        return paymentGateway



