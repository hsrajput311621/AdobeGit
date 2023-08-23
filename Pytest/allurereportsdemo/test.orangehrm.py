
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import allure_pytest
import time

class orangeHRM:
    def test_logo(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        logo = self.driver.find_element(By.XPATH, "//img[@alt='company-branding']").is_displayed()
        if logo == "OrangeHRM":
            assert True
        else:
            assert False

        self.driver.close()


    def test_employes(self):
        pytest.skip("testing is skipped for time being")

    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        act_title = self.driver.title
        if act_title == "OrangeHRM":
            assert True
        else:
            assert False

        self.driver.close()

