from selenium.webdriver.common.by import By

from PageObjects.FlightFarePage import FlightFarePage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    fromLocation = (By.NAME, "flight_origin")
    toLocation = (By.NAME, "flight_destination")
    originDate = (By.ID, "BE_flight_origin_date")
    selectDate = (By.ID, "27/02/2021")
    searchButton = (By.ID, "BE_flight_flsearch_btn")

    def getFromLocation(self):
        return self.driver.find_element(*HomePage.fromLocation)

    def getToLocation(self):
        return self.driver.find_element(*HomePage.toLocation)

    def getOriginDate(self):
        return self.driver.find_element(*HomePage.originDate)

    def getSelectdate(self):
        return self.driver.find_element(*HomePage.selectDate)

    def getSearchButton(self):
        self.driver.find_element(*HomePage.searchButton).click()
        flightFarePage = FlightFarePage(self.driver)
        return flightFarePage













