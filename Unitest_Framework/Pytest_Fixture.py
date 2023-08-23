
# How to work with Pytest Fixture!

# The purpose of thest fixtures is to provide a fixed baseline upon which tests can reliably and repeatedly execute.

#@pytest.fixture() : Executes specific method before every test method.
#@pytest.yield_fixture(): Execute specific method before & After every test method.

import pytest

@pytest.fixture()
def setup():
    print("Once before every method")

def testmethod1(setup):
    print("This is the test method1")

def testmethod2(setup):
    print("This is the test method2")


@pytest.yield_fixture()
def setup2():
    print("This method will execute before of the other methods")
    yield
    print("Once After every method")

def testmethod11(setup2):
    print("This is the test method1")

def testmethod12(setup2):
    print("This is the test method2")