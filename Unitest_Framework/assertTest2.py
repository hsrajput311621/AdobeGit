#assertTrue : when we have only two parameter we can se assertEqual method of check both are same or not, but
# if we have more than two parameters, comparing values with assertEqual method become more difficult.
#asserTrue method checks whether given parameter is true or not, if value is true then test is passed otherwise test failed/


#assertFalse:
#assertFalse method compares whether given value or expression results in false or not,
# If the result or value is False then unittest passes the testcase but if the result or value is Ture then unittest fails the test case.


import unittest
from selenium import  webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="Location of the driver")
        driver.get("URL")
        titleofwebpage = driver.title
        self.assertTrue(titleofwebpage == "Google")
        # self.assertFalse(titleofwebpage == "Google")


if __name__=="__main__":
    unittest.main()

