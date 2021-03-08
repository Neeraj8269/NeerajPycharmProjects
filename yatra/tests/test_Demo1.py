import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

# from utilities.BaseClass import BaseClass
# from TestData.test_data import TestData
from TestData.test_data import TestData
# from utilities.BaseClass import BaseClass
import pyautogui as pg

driver = None


class TestDemo(TestData):
    def test_form_submission(self, get_data_new):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()
        # driver.set_window_size(1366, 768)
        time.sleep(3)
        # driver.implicitly_wait(15)
        # driver.maximize_window()
        # driver.find_element_by_name("name").send_keys(get_data_new["Firstname"])
        # driver.find_element_by_name("email").send_keys(get_data_new["Lastname"])
        # driver.find_element_by_xpath("//div[@class='form-group'][3]/input").send_keys("Test@123")
        # dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
        # dropdown.select_by_visible_text(get_data_new["Gender"])
        # driver.find_element_by_tag_name("html").send_keys(Keys.END)
        driver.execute_script("window.scrollTo(0, 500)")

        pg.moveTo(1340, 51, 4)
        pg.click(1340, 51)
        time.sleep(5)
        driver.refresh()








