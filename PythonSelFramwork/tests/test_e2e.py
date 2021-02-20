import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.CheckOutPage import CheckOutPage
from utilities.BaseClass import BaseClass
from PageObjects.HomePage import HomePage


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        self.driver.implicitly_wait(2)
        checkOutPage = homePage.getshopItems()
        log.info("getting all the card titles")
        # checkOutPage = CheckOutPage(self.driver)
        products = checkOutPage.getCardTitles()
        for product in products:
            ProductName = product.find_element_by_xpath("div/h4/a").text
            if ProductName == "Blackberry":
                product.find_element_by_xpath("div/button").click()

        checkOutPage.getCheckOutButton().click()
        confirmPage = checkOutPage.getFinalCheckout()
        log.info("Entering the location as India")
        confirmPage.getEnterLocation().send_keys("ind")
        self.verifyLinkPresence("India")
        confirmPage.getSelectIndia().click()
        # driver.find_element_by_xpath("//a[contains(text(),'India')]").click()
        confirmPage.getCheckBox().click()
        confirmPage.getPurchaseButton().click()
        SuccessAlertText = confirmPage.getPrintSuccessText().text
        log.info("Success alert text received which is "+SuccessAlertText)
        print(confirmPage.getPrintSuccessText().text)
        SuccessAlert = confirmPage.getPrintSuccessText().text
        assert "Your order will be" in SuccessAlert
