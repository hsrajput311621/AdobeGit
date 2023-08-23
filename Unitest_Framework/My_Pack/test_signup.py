
import pytest

@pytest.fixture()
def setup():
    print("Opening URL to signup")
    yield
    print("Closing browse to signup")

def test_signupbyemail(setup):
    print("This is the signup by email")

def test_signupbyfacebook(setup):
    print("This is the signup by facebook")

