import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
price_range = driver.find_elements_by_xpath("//*[@id='mega-filter-open-close-price'][4]/div/div/div/div/div/ul/li/label")
# for new_range in price_range:
#     if "Rs. 7,001 to Rs. 10,000" in new_range.text:
#         new_range.click()
#         break

hotel_box = driver.find_elements_by_xpath("//div[@class='result-details-wrapper full']")
for names in hotel_box:
    hotel_name = names.find_element_by_xpath("div/div/h2").text
    if "Citrus Prime Bhopal" in hotel_name:
        names.find_element_by_xpath("div[2]/div/span").click()
    # driver.find_element_by_tag_name("html").send_keys(Keys.END)

ChildWindow = driver.window_handles[1]
driver.switch_to.window(ChildWindow)

# driver.find_element_by_tag_name("view more ")

book_now_box = driver.find_elements_by_xpath("//li[@class='row cr-det']")
for book in book_now_box:
    book_facility = book.find_element_by_xpath("div/div[1]/span[1]").text
    print(book_facility)
    if "Premier King Bedroom Double - Room Only" in book_facility:
        book.find_element_by_xpath("div[2]/div[5]/button").click()










