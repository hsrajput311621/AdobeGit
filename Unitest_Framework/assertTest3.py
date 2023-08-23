
#assertIsNone: method verifies whether given values or expression results in None or not, if the result is none
# then python unittest will pass the test case otherwise fails the testcase.

#assertNotNone: method verifies whether givn values is not None, if the value is None then the test case will be failed.

import unittest
from selenium import  webdriver

class Teat(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="location of web browser")
        self.assertIsNone(driver)
        self.assertIsNotNone(driver)
        

if __name__ == "__main__":
    unittest.main()

