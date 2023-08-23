
# Python UnitTest Framework:
#1) Setup
#2) Teardown
#3) SetUpClass
#4) TearDownClass
#5) TearDownModule

#1) Setup : This is the method which execute  many times before executing the actual test methods.
# it can be use to initialize the driver method, as we need to call webdriver/driver everytime
# before the acutal test case is executed.

#2) Teardown Method: It is reciprocal to setup methods, it is called multiple time
# , after the acutual test will execute. so if we have 100 test cases,
# then Setup and Teardown method will execute 100 times.

