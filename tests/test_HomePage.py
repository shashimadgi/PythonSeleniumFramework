import time

from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        log = self.getLogger()
        homepage= HomePage(self.driver)
        log.info("first name is "+getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getCheckBox().click()
        # Safely handle missing 'gender' with a default value
        # gender = getData.get("gender", "Male")
        # log.info(f"Selecting gender: {gender}")
        self.selectOptionByText(homepage.getGender(), "Male")
        homepage.submitForm().click()
        time.sleep(5)

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase1"))
    def getData(self, request):
        return request.param

