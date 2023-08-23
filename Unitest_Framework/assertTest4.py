
# assertIn : method verifies whether the first element is present in the send element, if first element is present in
# second element then test is passed otherwise test is failed.

# assertNotIn: method verifies, whether the first element is not present in the second element or not,
# if first element ispresent then test will be faild otherwise test is passed.

#These two methods will be helpful when you want to verify presence of a value in a list, tuple, set and dictionalry.

import unittest

class Test(unittest.TestCase):
    def testName(self):
        list=("python", "selenium", "jave")
        self.assertIn("python", list)  # pass the test ase
        self.assertIn("ruby", list)  #failed the test case

        self.assertNotIn("python", list)   #failed
        self.assertNotIn("(eupy")


if __name__=="__main__":
    unittest.main()
