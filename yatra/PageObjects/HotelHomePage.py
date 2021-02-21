from selenium.webdriver.common.by import By

from PageObjects.HotelListPage import HotelListPage


class HotelHomePage:
    def __init__(self, driver):
        self.driver = driver

    Go_Hotel_Page = (By.ID, "booking_engine_hotels")
    FieldDestination = (By.NAME, "BE_hotel_destination")
    ClearText = (By.NAME, "BE_hotel_destination")
    inputDestination = (By.NAME, "BE_hotel_destination")
    checkInField = (By.ID, "BE_hotel_checkin_date")
    checkInDate = (By.ID, "23/02/2021")
    checkOutField = (By.ID, "BE_hotel_checkout_date")
    checkOutDate = (By.ID, "26/02/2021")
    searchButton = (By.ID, "BE_hotel_htsearch_btn")

    def get_go_hotel_page(self):
        return self.driver.find_element(*HotelHomePage.Go_Hotel_Page)

    def get_field_destination(self):
        return self.driver.find_element(*HotelHomePage.FieldDestination)

    def get_clear_text(self):
        return self.driver.find_element(*HotelHomePage.ClearText)

    def get_input_destination(self):
        return self.driver.find_element(*HotelHomePage.inputDestination)

    def get_check_in_field(self):
        return self.driver.find_element(*HotelHomePage.checkInField)

    def get_check_in_date(self):
        return self.driver.find_element(*HotelHomePage.checkInDate)

    def get_check_out_field(self):
        return self.driver.find_element(*HotelHomePage.checkOutField)

    def get_check_out_date(self):
        return self.driver.find_element(*HotelHomePage.checkOutDate)

    def get_search_button(self):
        self.driver.find_element(*HotelHomePage.searchButton).click()
        hotel_list_page = HotelListPage(self.driver)
        return hotel_list_page









