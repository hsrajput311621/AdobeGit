

# We are working on small projects : Selenium Unit test, PageObject Model, HRML Reports.
#UnittestPOMBasedProject
#Drivers - pagePbjects - TestCases - Reports

# Test Case:
#1) Launch chrome browser.
#2) open URL : http://admin-demo.nopcommerce.com/
#3) Provide username: admin@yourstore.com
#4) Provide password: admin
#5) click on login
#6)Expected title : Dashboard /nopCommerce administration.

from selenium import webdriver
import unittest

class LoginPage():  # Locators of all the elements
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@type='submit']"
    button_logout_xpath = "//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver = driver
        self.driver = webdriver.Chrome()
        self.driver.get("http://admin-demo.nopcommerce.com/")

    def setUserName(self, username):
        self.driver.find_element(BY.ID, "textbox_username_id").clear()
        self.driver.find_element(BY.ID, "textbox_username_id").send_keys(username)

    def setPasswordName(self, password):
        self.driver.find_element(By.ID, "textbox_password_id").clear()
        self.driver.find_element(By.ID, "textbox_password_id").send_keys(password)

    def clickLogin(self):
        self.driver.find_element(BY.XPATH, "button_login_xpath").click()

    def clickLogout(self):
        self.driver.find_element(BY.XPATH, "button_logout_xpath").click()





