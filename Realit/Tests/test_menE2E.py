import time
import pyautogui as pg
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://app.reelit.ninja/login')
driver.maximize_window()
driver.implicitly_wait(15)
driver.find_element_by_css_selector("input[placeholder='Email']").send_keys("testing9934@gmail.com")
driver.find_element_by_css_selector("input[placeholder='Password']").send_keys("Test@123")
driver.find_element_by_css_selector("button[type='submit']").click()
time.sleep(3)
driver.find_element_by_css_selector("a[fragment='category-men']").click()
driver.find_element_by_xpath("//img[@src='//images.ctfassets.net/ljoz65y94szt/6NCyS7BqDZ9plqU0WhqPd6/7dacf797b732c1ef96a9b63d7990b9e3/Men_Boots.jpg']").click()
time.sleep(4)
# checkbox = driver.find_elements_by_xpath("//span[contains(text(),'New Arrivals')]")
# for checkboxName in checkbox:
#     if checkboxName.text == "New Arrivals":
#         checkboxName.click()


productList = driver.find_elements_by_xpath("//p[@class='title font-bold text-xxs md:text-sm']")
print(len(productList))
for names in productList:
    # productName = names.find_elements_by_xpath("div/p[1]")
    print(names.text)
    if "THE TIRE BOO" in names.text:
        driver.find_element_by_xpath("//div[@class='image ng-lazyloaded']").click()
        break

pg.moveTo(1246, 412)

driver.find_element_by_xpath("//div[contains(text(),'SIZE')]").click()
driver.find_element_by_xpath("//div[@class='hidden show-option']/ul/li[3]/span[1]").click()
driver.find_element_by_css_selector("span[class='underline']").click()
time.sleep(4)
driver.find_element_by_xpath("//span[contains(text(),'PROCEED TO CHECKOUT')]").click()
time.sleep(2)
driver.find_element_by_xpath("//span[contains(text(),'DEBIT CARD')]").click()
time.sleep(4)
driver.find_element_by_name("name").send_keys("Testing Now")
driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='card-number-element']/div/iframe"))
driver.find_element_by_name("cardnumber").send_keys("4242424242424242")
# driver.switch_to.default.content()
# driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='card-expiry-element']/div/iframe"))
driver.find_element_by_xpath("//*[@id='root']/form/span[2]/span/input").send_keys("0223")
# driver.switch_to.default.content()
driver.find_element_by_name("exp-date").send_keys(Keys.TAB)
driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='card-cvc-element']/div/iframe"))
driver.find_element_by_name("cvc").send_keys("123")
# driver.switch_to.default.content()
driver.find_element_by_name("cvc").send_keys(Keys.TAB)
driver.find_element_by_name("postal_code").send_keys("10001")



# sizeList = driver.find_elements_by_xpath("//div[@class='hidden show-option']/ul")
# for size in sizeList:
#     print(size.text)
#     if size.text == "13":
#         size.click()
#         break














