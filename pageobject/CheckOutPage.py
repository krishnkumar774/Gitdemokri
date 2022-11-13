from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver
        # driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    CardTitle = (By.XPATH, "//div[@class='card h-100']")
    #self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']")
    #self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']")

    checOt= (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkSucess = (By.XPATH, "//button[@class='btn btn-success']")

    #find_element(By.XPATH, "div/h4/a")
    p1 = (By.XPATH, "div/h4/a")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.CardTitle)

    def CheckBuy(self):
        return self.driver.find_element(*CheckOutPage.checOt)
    def CheckSucess(self):
        return self.driver.find_element(*CheckOutPage.checkSucess)
    def getp1(self):
        return self.driver.find_element(*CheckOutPage.p1)




