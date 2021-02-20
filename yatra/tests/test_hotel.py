import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.yatra.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_id("booking_engine_hotels").click()
driver.find_element_by_name("BE_hotel_destination").click()
time.sleep(1)
driver.find_element_by_name("BE_hotel_destination").clear()
driver.find_element_by_name("BE_hotel_destination").send_keys("Bhopal")
time.sleep(2)
driver.find_element_by_name("BE_hotel_destination").send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_id("BE_hotel_checkin_date").click()
time.sleep(2)
driver.find_element_by_id("23/02/2021").click()
driver.find_element_by_id("BE_hotel_checkout_date").click()
driver.find_element_by_id("26/02/2021").click()
driver.find_element_by_id("BE_hotel_htsearch_btn").click()
price_range = driver.find_elements_by_xpath(
    "//*[@id='mega-filter-open-close-price'][4]/div/div/div/div/div/ul/li/label")

for new_range in price_range:
    if "Rs. 7,001 to Rs. 10,000" in new_range.text:
        new_range.click()
        break

time.sleep(2)
hotel_box = driver.find_elements_by_xpath("//div[@class='result-details-wrapper full']")
for names in hotel_box:
    hotel_name = names.find_element_by_xpath("div/div/h2").text
    if "Hotel Sarthak" in hotel_name:
        names.find_element_by_xpath("div[2]/div/span").click()
    # driver.find_element_by_tag_name("html").send_keys(Keys.END)

ChildWindow = driver.window_handles[1]
driver.switch_to.window(ChildWindow)
time.sleep(2)
# driver.find_element_by_tag_name("view more ")

driver.find_element_by_css_selector("a[class='uprcse ml10']").click()

book_now_box = driver.find_elements_by_xpath("//li[@class='row cr-det']")
for book in book_now_box:
    book_facility = book.find_element_by_xpath("div/div[1]/span[1]").text
    if "Deluxe Single Room" in book_facility:
        book.find_element_by_xpath("div[2]/div[5]/button").click()
        break

time.sleep(5)
driver.find_element_by_name("additionalContactEmail").send_keys("neeraj871@gmail.com")
driver.find_element_by_name("additionalContactMobile").send_keys("8269606807")
handlel_dropdown = Select(driver.find_element_by_name("title0"))
handlel_dropdown.select_by_value("Mr")
driver.find_element_by_name("fname0").send_keys("Neeraj Kumar")
driver.find_element_by_name("lname0").send_keys("Singh")
time.sleep(5)
driver.find_element_by_css_selector("div[class*='sticky-sm-bottom'] button:nth-child(1)").click()
driver.find_element_by_id("amazonPay").click()
driver.find_element_by_id("amazonPay").click()


















