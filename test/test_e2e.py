
from selenium.webdriver.common.by import By


from pageobject.CheckOutPage import CheckOutPage
from pageobject.ConfirmPage import ConfirmationPage
from pageobject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):        # Inharitance  child class

    def test1_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.shopItem().click()
        log.info("Getting all card added")
        checkoutpage =CheckOutPage(self.driver)
        products = checkoutpage.getCardTitles()
        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            log.info(productName)
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

        checkoutpage.CheckBuy().click()
        checkoutpage.CheckSucess().click()

        confirmationPage = ConfirmationPage(self.driver)
        confirmationPage.fillParameter().send_keys("Ind")
         #Wait
        self.verifiedLinkTest("India")

        confirmationPage.SelectTestVAlue().click()
        confirmationPage.getPurchege().click()
        text1 = confirmationPage.testVaueMatch().text
        log.info("test is ="+ text1)
        assert "Success! Thank you!" in text1
