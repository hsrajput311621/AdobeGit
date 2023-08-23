# This is a pageObject class module

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readproperties import ReadConfig

class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/"
#    baseURL = ReadConfig.getApplicationURL()
    username = "admin@yourstore.com"
#    username = ReadConfig.getUseremail()
#    password = ReadConfig.getUserpassword()
    password = "admin"
#We have to create two test cases, one is Homepage title,and username and password test.

    def test_homePageTitle(self,setup): #here we have created fixture so that,
     #  self.driver = webdriver.Chrome()    # we do not need to initialize driver everytime
        self.driver = setup     # setup is name of the method created for driver
        self.driver.get(self.baseURL)  #picking baseurl from variable
        actual_title = self.driver.title  # capturing title of page
        self.driver.close()
        if actual_title == "Your store. Login":
            assert  True
            self.driver.close()
        else:
#            self.driver.save_screenshot(".\\Screenshots"+"test_homePageTitle.png")
            assert False
            self.driver.close()

    def test_login(self,setup):
        #self.driver = webdriver.Chrome()
        self.driver = setup   # same fixture called for driver
        self.driver.get(self.baseURL)  # assinging baseURL from variable
        self.lp=LoginPage(self.driver) # creating object 'lp' of class LoginPage, to call constructor and methods
        self.lp.setUserName(self.username) # giving parameter username to method in LoginPAge class
        self.lp.setPassword((self.password)) # assigning password to method in LoginPage class
        self.lp.clickLogin()  # object lp for click for login
        actual_title = self.driver.title
        self.driver.close()
        if actual_title == "Dashboard / nopcommerce administration":
            assert True
        else:
#           self.driver.save_screenshot(".\\Screenshot\\" + "test_login.png")
            assert False
            self.driver.close()




