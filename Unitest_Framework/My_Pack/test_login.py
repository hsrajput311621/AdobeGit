import pytest

@pytest.fixture()
def setup():
    print("Opening URL to Login")
    yield
    print("Closing browser after login")

def test_loginByemail(setup):
    print("This is Login by email test")

def test_loginbyfacebook(setup):
    print("This is the login by facebook test")

