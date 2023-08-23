import unittest
from selenium import webdriver
import HtmlTestRunner
import time
from pageObjects.LoginPage import LoginPage
import sys
sys.path.append("D:/PYTHON-PROJECTS/PythonUnitTestProject_POMBased")

class LoginTest(unittest.TestCase):
    base_url = "http://admin-demo.nopcommerce.com/"
    usernmae = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        cls.driver.get(base_url)
        cls.driver.maximize_window()


    def test_login(self):
        lp = LoginPage(self.driver)
        lp.setUserName(self.usernmae)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)
        self.assertEqual("Dashboard / nopCommerce administration", self.driver.title, "webpage title is not match")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output ="..\\reports"))










