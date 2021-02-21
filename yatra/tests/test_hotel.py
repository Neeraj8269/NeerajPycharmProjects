import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from PageObjects.HomePage import HomePage
from PageObjects.HotelHomePage import HotelHomePage
from utilities.BaseClass import BaseClass
from PageObjects.CheckOutPage import CheckOutPage


class Test_Hotel_Booking(BaseClass):
    def test_hotel_booking(self):
        self.driver.implicitly_wait(15)
        log = self.getLogger()
        hotelHomePage = HotelHomePage(self.driver)
        hotelHomePage.get_go_hotel_page().click()
        hotelHomePage.get_field_destination().click()
        hotelHomePage.get_clear_text().clear()
        time.sleep(1)
        hotelHomePage.get_input_destination().send_keys("Bhopal")
        hotelHomePage.get_input_destination().send_keys(" Madhya Pradesh")
        time.sleep(2)
        log.info("Location is entered")
        hotelHomePage.get_field_destination().send_keys(Keys.ENTER)
        time.sleep(2)
        hotelHomePage.get_check_in_field().click()
        time.sleep(2)
        hotelHomePage.get_check_in_date().click()
        hotelHomePage.get_check_out_field().click()
        time.sleep(1)
        hotelHomePage.get_check_out_date().click()
        hotel_list_page = hotelHomePage.get_search_button()
        price_range = hotel_list_page.get_price_range_list()

        for new_range in price_range:
            if "Rs. 7,001 to Rs. 10,000" in new_range.text:
                new_range.click()
                break

        time.sleep(2)
        hotel_name_list = hotel_list_page.get_select_hotel_list()
        for names in hotel_name_list:
            hotel_name = names.find_element_by_xpath("div/div/h2").text
            if "Hotel Sarthak" in hotel_name:
                names.find_element_by_xpath("div[2]/div/span").click()
            # driver.find_element_by_tag_name("html").send_keys(Keys.END)

        ChildWindow = self.driver.window_handles[1]
        self.driver.switch_to.window(ChildWindow)
        time.sleep(2)
        hotel_list_page.get_view_more_button().click()

        room_types = hotel_list_page.get_room_types()
        for book in room_types:
            book_facility = book.find_element_by_xpath("div/div[1]/span[1]").text
            if "Deluxe Single Room" in book_facility:
                book.find_element_by_xpath("div[2]/div[5]/button").click()
                break

        time.sleep(5)
        check_out_page = CheckOutPage(self.driver)
        check_out_page.get_hotel_input_email().send_keys("neeraj871@gmail.com")
        check_out_page.get_hotel_input_mobile().send_keys("9870466369")
        handlel_dropdown = Select(check_out_page.get_hotel_select_dropdown())
        handlel_dropdown.select_by_value("Mr")
        check_out_page.get_hotel_input_firstname().send_keys("Neeraj Kumar")
        check_out_page.get_hotel_input_lastname().send_keys("Singh")
        time.sleep(5)
        paymentGateway = check_out_page.get_proceed_to_payment_button()
        time.sleep(1)
        paymentGateway.getAmazonPayment().click()
        paymentGateway.getAmazonPayment().click()


