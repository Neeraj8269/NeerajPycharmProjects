from selenium.webdriver.common.by import By

from PageObjects.CheckOutPage import CheckOutPage


class HotelListPage:
    def __init__(self, driver):
        self.driver = driver

    price_range_list = (By.XPATH, "//*[@id='mega-filter-open-close-price'][4]/div/div/div/div/div/ul/li/label")
    select_hotel_list = (By.XPATH, "//div[@class='result-details-wrapper full']")
    view_more_button = (By.CSS_SELECTOR, "a[class='uprcse ml10']")
    room_types = (By.XPATH, "//li[@class='row cr-det']")

    def get_price_range_list(self):
        return self.driver.find_elements(*HotelListPage.price_range_list)

    def get_select_hotel_list(self):
        return self.driver.find_elements(*HotelListPage.select_hotel_list)

    def get_view_more_button(self):
        return self.driver.find_element(*HotelListPage.view_more_button)

    def get_room_types(self):
        return self.driver.find_elements(*HotelListPage.room_types)


