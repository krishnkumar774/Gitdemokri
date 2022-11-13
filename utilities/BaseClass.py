import inspect

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import logging

@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
            loggerName =inspect.stack()[1][3]
            logger = logging.getLogger(loggerName)
            filehandler = logging.FileHandler('logfile.log')
            formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
            filehandler.setFormatter(formatter)
            logger.addHandler(filehandler)
            logger.setLevel(logging.DEBUG)
            return logger

    def verifiedLinkTest(self,text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))