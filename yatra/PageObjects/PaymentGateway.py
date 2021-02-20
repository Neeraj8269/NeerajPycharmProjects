from selenium.webdriver.common.by import By


class PaymentGateway:
    def __init__(self, driver):
        self.driver = driver

    amazonPayment = (By.ID, "amazonPay")

    def getAmazonPayment(self):
        return self.driver.find_element(*PaymentGateway.amazonPayment)
