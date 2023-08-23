

# This is the 2nd test case of package2:

import unittest

class PaymentReturnsTest(unittest.TestCase):
    def test_paymentReturnbybank(self):
        print("This is the method to return money by bank")
        self.assertTrue(True)


if __name__=="__main__":
    unittest.main()

