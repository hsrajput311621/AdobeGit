import unittest

def setUpModule(): #It will executed before executing any class or any method present in the test class
    print("setupModule")

def tearDownModule(): # Itv will executed after completing everything present in the python module.
    print("tearDownModule")

class AppTesting(unittest.TestCase):
    #setup method is mainly use for driver to launch browser.

    @classmethod
    def setUp(self):
        print("This is login test")

    @classmethod
    def tearDown(self):
        print("This is the logout test")

    @classmethod
    def setUpClass(cls) -> None:  # Executed once when the class started.
        print("Open Application")

    @classmethod
    def tearDownClass(cls) -> None:  # Executed once after the class completed.
        print("Close application")

    def test_search(self):
        print("This is the search test")

    def test_advancesearch(self):
        print("This is the advance search test")

    def test_prepaidRecharge(self):
        print("This is prepaid Recharge test")

    def test_postpaidRecharge(self):
        print("This is post paidRecharge test")

if __name__== "__main__":
    unittest.main()




