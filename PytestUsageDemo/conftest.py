from pytest import fixture
from selenium import webdriver


@fixture(scope="session")
def chrome_browser():
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/#/index")
    driver.maximize_window()
    driver.implicitly_wait(15)
    yield driver
    driver.close()
