from selenium.webdriver.support.select import Select


class DemoPage:
    def selectMrDropdown(self, text):
        dropdown_handle = Select(self.driver.find_element_by_name("title0"))
        dropdown_handle.select_by_value(text)

