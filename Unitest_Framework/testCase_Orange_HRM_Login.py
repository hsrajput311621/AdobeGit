
# Python unittest HTML TestRunner Reports
# Selenium Python Test Case using Unit Test, HTML Reports.
# Selenium Python Project | Unit Test, POM, HTML Reports
#-------------------------------------

#html-testRunner

#--------------------
# Test Case Orange HRM login Test
# Launch Browser
# Verify home page title
#verify login
#close browser

# we use setUpClass(): execute one time it will execute one time before all the methods are executed

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest

import HtmlTestRunner

class OrangeHRMtest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_homePageTitle(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.assertEqual("OrangeHRM",self.driver.title, "webpage is not matching")

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.assertEqual("OrangeHRM",self.driver.title, "webpage is not matching")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test completed....")


if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\\PYTHON-PROJECTS\\Unitest_Framework\\Reports'))






