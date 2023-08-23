import unittest
from selenium import webdriver

class SearchEngine_TestCase(unittest.TestCase):    # we need to extend the parent class unittest for all the classes.
    def test_Google(self):                       #unittest.Testcase: Unittest class must be inherit by the test case class.
        self.driver = webdriver.Chrome()         # webdriver is calling the chrome
        self.driver.get("hhtps://www.google.com")                  # driver.get we use to add the URL of the website.
        print("The title of the page is "" ", self.driver.title)
        self.driver.close()

    def test_Bing(self):
        self.driver = webdriver.Chrome("")
        self.driver.get("https://www.bing.com")
        print("The title of the page is " " ", self.driver.title)
        self.driver.close()
        

if __name__== "__main__":
    unittest.main()
