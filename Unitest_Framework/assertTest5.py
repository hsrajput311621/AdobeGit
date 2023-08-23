#Rationa comparison!!
#assertGreater it varifies whether first values if greater than second value of not

#assertGreaterEqual: verifies whether first parameter is greater or equal to second parameter.

# assertLess: it verifies whether parameter is lesser than second parameter or not.

#assertLessEqual: it verifies whether first parameter is lesser or equal to the second parameter.

import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        self.assertGreater(100,10)  # passed as 100 is greater than 10
        self.assertGreaterEqual(100,100) # passes as 100 is equal to 100

    def Test2(self):
        self.assertLess(10,100)  # first number must less than 2nd number then passed.
        self.assertLessEqual(100,100) # first number must less or equal to second value.



if __name__=="__main__":
    unittest.main()
