import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name" ,action="store",default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    chrome_obj = webdriver.ChromeOptions()
    browser_name=request.config.getoption("browser_name")
    if browser_name=="chrome":
        service_obj = Service("C:\\prc\\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj, options=chrome_obj)
        chrome_obj.add_argument("--start-maximized")
    elif browser_name =="firefox":
        service_obj = Service("C:\\prc\\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    driver.get("https://rahulshettyacademy.com/angularpractice/")


    request.cls.driver = driver
    yield
    driver.close()
