# Create LoginPage Ojbect Class under "pageObjects"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class LoginPage:
    textbox_username_id="Email"     #Here we have added the locators of each elements
    textbox_password_id="Password"   # and store in the variable so that we can use
    button_login_xpath="//button[@type='submit']"  # them into the test case
    Link_logout_Linktext="Logout"      # these variables are not fixed we can chage the locators
                                    # name and use for the future cases.
    def __init__(self,driver):        # here we are expecting driver as paramneter from the test case
        self.driver=driver         # driver can be now use for whole class using self keyword

    def setUserName(self,username):   # created methods to receive the username from testcase
        self.driver.find_element_by_id (self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.Link_logout_Linktext).click()
