from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.color import Color

driver = webdriver.Chrome()
driver.get("https://www.lambdatest.com/blog/python-selenium-screenshots/")
driver.implicitly_wait(15)
driver.get_screenshot_as_file("pic.png")
color_value = driver.find_element_by_css_selector("span[class*='color-titel']").value_of_css_property('color')
print(color_value)
hexColor = Color.from_string(color_value).hex
print(hexColor)
driver.close()

# Act = ActionChains(driver)
        # Act.key_down(driver.find_element_by_name("bday"))
        # Act.key_down(driver.find_element_by_name("bday"))
# pytest --html=report.html

# payment_button = WebDriverWait(self.driver, 10)
#         payment_button.until(expected_conditions.presence_of_element_located(
#            (By.XPATH, "//button[contains(text(),'Proceed To Payment')]")))









