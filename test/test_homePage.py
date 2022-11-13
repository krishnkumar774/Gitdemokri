import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import testDataHomePage
from pageobject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getCheck().click()
        sel = Select(homepage.getGender())
        sel.select_by_visible_text(getData["gender"])
        homepage.getSubmit().click()
        alrtTest = homepage.getText().text
        assert ("Success" in alrtTest)
        self.driver.refresh()


    @pytest.fixture(params=testDataHomePage.gettestExcelData("Testcase2"))
    def getData(self,request):
        return request.param

