
# First Test case of Package2

import unittest
from selenium import webdriver

class PaymentTest(unittest.TestCase):
    def test_Paymentindollar(self):
        print("This is the payment method in dollar")
        self.assertTrue(True)

    def test_Paymentinruppes(self):
        print("This is the payment method in rupees")
        self.assertTrue((True))


if __name__=="__main__":
    unittest.main()


