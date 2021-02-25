import inspect
import logging
import pytest
# from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s, %(levelname)s, :%(name)s, %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    # def selectMrDropdown(self, text):
    #     dropdown_handle = Select(self.driver.find_element_by_name("title0"))
    #     dropdown_handle.select_by_value(text)










