
# Test_Case0002

import unittest
from selenium import webdriver

class SignupTest(unittest.TestCase):
    def test_Signupbyemail(self):
        print("This is the signup test by email")
        self.assertTrue(True)

    def test_Signupbyfacebook(self):
        print("This is the signup test by facebook")
        self.assertTrue(True)

    def test_Signupbytwitter(self):
        print("This is the signup test by twitter")
        self.assertTrue(True)



if __name__=="__main__":
    unittest.main()
