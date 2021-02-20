from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    enterLocation = (By.ID, "country")
    selectIndia = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchaseButton = (By.XPATH, "//input[@value='Purchase']")
    printSuccessText = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def getEnterLocation(self):
        return self.driver.find_element(*ConfirmPage.enterLocation)

    def getSelectIndia(self):
        return self.driver.find_element(*ConfirmPage.selectIndia)

    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def getPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

    def getPrintSuccessText(self):
        return self.driver.find_element(*ConfirmPage.printSuccessText)



