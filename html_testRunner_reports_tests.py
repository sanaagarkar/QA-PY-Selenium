# Installing 'html test runner' package: 'pip install html-testRunner'
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  # Import By
import time

# Importing the package:
import HtmlTestRunner


class LoginTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_01_searching_in_goolge(self):
        self.driver.get("https://www.google.com")
        self.driver.implicitly_wait(10)
        elem = self.driver.find_element(By.NAME, "q")  # Updated method
        elem.send_keys("Selenium")
        elem.submit()
        self.assertIn("Selenium", self.driver.title)

    @classmethod
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    # 'html testRunner' package code execution
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Programming/QA/Projects/qa-automation/qa-py-selenium-simple-usage/reports'))