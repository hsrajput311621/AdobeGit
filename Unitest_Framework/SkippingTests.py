
import unittest

class Apptesting(unittest.TestCase):

    @unittest.SkipTest    # it is called decorator this is use to skip the particula test and it will execute rest ones
    def test_search(self):
        print("This is the search test")

    def test_advancedsearch(self):
        print("This is an adv search test")

    @unittest.skip("I am skipping this test bcoz it not ready yet")
    def test_postpaidrecharge(self):
        print("This is the pre-paid test")

    def test_prepainrecharge(self):
        print("This is the postpaid test")

    @unittest.skipIf(1==1, "One is not equal to one")
    def test_loginbygmail(self):
        print("This is a login by gmail test")

    def test_loginbytwitter(self):
        print("This is a login by twitter test")

if __name__ == "__main__":
    unittest.main


