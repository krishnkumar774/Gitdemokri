from selenium.webdriver.common.by import By


class ConfirmationPage:
    def __init__(self, driver):
        self.driver = driver
    Parmeter =(By.ID, "country")
    # self.driver.find_element(By.LINK_TEXT, "India")
    selectTest =(By.LINK_TEXT, "India")
    # self.driver.find_element(By.CSS_SELECTOR, "[value='Purchase']").
    Purchage = (By.CSS_SELECTOR, "[value='Purchase']")
    # self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-dismissible']")
    TestvalueMatch = (By.CSS_SELECTOR, "[class*='alert-dismissible']")

    def fillParameter(self):
        return self.driver.find_element(*ConfirmationPage.Parmeter)
    def SelectTestVAlue (self):
        return self.driver.find_element(*ConfirmationPage.selectTest)
    def getPurchege(self):
        return self.driver.find_element(*ConfirmationPage.Purchage)
    def testVaueMatch(self):
        return self.driver.find_element(*ConfirmationPage.TestvalueMatch)

    def testVaueMatch11111111111111111111(self):
        return self.driver.find_element(*ConfirmationPage.TestvalueMatch)
    def testVaueMatch444444444444444444445556777(self):
        return self.driver.find_element(*ConfirmationPage.TestvalueMatch)
    def testVaueMatch49999999999999999999999(self):
        return self.driver.find_element(*ConfirmationPage.TestvalueMatch)

    def testVaueMatch10010101010101(self):
        return self.driver.find_element(*ConfirmationPage.TestvalueMatch)


