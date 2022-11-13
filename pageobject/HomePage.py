from selenium.webdriver.common.by import By

from pageobject.CheckOutPage import CheckOutPage


class HomePage:
    def __init__(self, driver):    # constructor
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    #driver.find_element(By.NAME, "name").send_keys("RAM")
    #driver.find_element(By.CSS_SELECTOR, "input[name='email']")
    #driver.find_element(By.ID, "exampleCheck1").click()
    #print(driver.find_element(By.CLASS_NAME, "alert-success")
    name = (By.NAME, "name")
    email =(By.CSS_SELECTOR, "input[name='email']")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    text = (By.CLASS_NAME, "alert-success")

    def shopItem(self):
        return self.driver.find_element(*HomePage.shop)
    def getName(self):
        return self.driver.find_element(*HomePage.name)
    def getEmail(self):
        return self.driver.find_element(*HomePage.email)
    def getCheck(self):
        return self.driver.find_element(*HomePage.check)
    def getGender(self):
        return self.driver.find_element(*HomePage.gender)
    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)
    def getText(self):
        return self.driver.find_element(*HomePage.text)
