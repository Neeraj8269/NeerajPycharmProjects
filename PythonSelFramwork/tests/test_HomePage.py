import pytest
from PageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageDy
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_homePage(self, getData):
        log = self.getLogger()
        self.driver.implicitly_wait(2)
        homepage = HomePage(self.driver)
        log.info("first name is "+getData["FirstName"])
        homepage.getName().send_keys(getData["FirstName"])
        homepage.getEmail().send_keys(getData["LastName"])
        homepage.getPassword().send_keys("Test@123")
        homepage.getCheckbox().click()
        self.SelectGender(homepage.getGender(), getData["Gender"])
        homepage.getSubmitButton().click()
        self.driver.refresh()

    @pytest.fixture(params=HomePageDy.home_Page_Data)
    def getData(self, request):
        return request.param



