import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import allure

class OrangeHRM:

    def test_logo(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        status = self.driver.find_element(By.XPATH, "//img[@alt='company-branding']").is_displayed()
        if status == True:
            assert True
        else:
            assert False

        self.driver.close()


    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.NAME,"username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        act_title = self.driver.title
        if act_title == "OrangeHRM":
            assert True
        else:
            assert False

        self.driver.close()



    def test_listemp(self):

        pytest.skip("The method is skipping for now")

