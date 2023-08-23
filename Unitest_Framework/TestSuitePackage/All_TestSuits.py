

# Here are need to import the test cases from the packages 1 and 2 to run the test cases with the help of test suite.


import unittest

from Package1.TC_LoginTest import LoginTest
from Package1.TC_SighnupTest import SignupTest

from Package2.TC_PaymentReturn import PaymentReturnsTest
from Package2.TC_PaymentTest import PaymentTest

# Get all teste from LoginTest, signupTest, PaymentReturns, PaymentTest.

t1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
t2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
t3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
t4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

# Creating Test Suits:

sanity_test_Suite = unittest.TestSuite([t1,t2])     # Sanity Test Suite
functionalTestSuite= unittest.TestSuite([t3, t4])  # functional testing
masterTestSuite = unittest.TestSuite([t1,t2,t3,t4]) # all the test cases in the full testing

unittest.TextTestRunner(verbosity=2).run(masterTestSuite)


