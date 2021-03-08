import time

from pytest import fixture, mark
from selenium import webdriver
from selenium.webdriver.support.color import Color


# @fixture()
# def chrome_browser():
#     driver = webdriver.Chrome()
#     driver.get("https://www.lambdatest.com/blog/python-selenium-screenshots/")
#     driver.maximize_window()
#     driver.implicitly_wait(15)
#     yield
#     driver.close()


@mark.selenium_example
def test_color_property(chrome_browser):
    driver = chrome_browser
    driver.find_element_by_link_text("Courses").click()
    time.sleep(4)


@mark.selenium_example
def test_Click_Live_menu(chrome_browser):
    driver = chrome_browser
    driver.find_element_by_xpath("//a[contains(text(),'Mentorship')]").click()
    time.sleep(4)

