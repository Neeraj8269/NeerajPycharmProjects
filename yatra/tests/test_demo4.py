from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys("thales")
names = driver.find