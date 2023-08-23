## Selenium Hybrid Framework###


# What is framework?
# Framework is an organized way of maintaining automation file. In the framework all th files will communicate each other to perform cretain task.

# Objective/Goals of Framework:
#1) Re-usability
#2) Maintainability

# Types of Framework:
# 1) Built-in framwworks: (Pytest, Robotframework, unitest etc)
# 2) Customized/User-defined Framework : Datadriven framework, keyword driven framework, Hybrid driven framework.

# Phases of the Framework:
#1) Analyze application, technology & skill set of team, Choose the test cases.


#Q) What are reason to choose the test cases for the Automation in the selenium?
#A) The main testcases will be Re-testing and Regression Test cases, those test which can be automatable.

#2) Design and implimentation of framework

#3) Exectution the framework with help of Maven, jenkins and the other utilites.

#4) Maintainance of the framework.

# What type of test cases we generally automate?
#1) Re-test cases(Test Data).
#2) Re-gression Cases.
#3) Test Cases can be automatable.

#Automation will be performed in E-Commerce platform:
#1)Frontend, and Backend:

#website Link: www.admin-demo.nopcommerce.com

#Step1: Create new project & Install required package/plugins
#a) Selenium: Selenium libraries.
#b) Pytest: Python Unittest framework.
#c) Pytest-html:Pytest HTML reports.
#d) pytest-xdist: Run test paralles.
#e) openpyxl: MS Excel support.
#f) Allure-pytest: tp generate allure reports.

#Step2: Create Folder Structure:
#Project Name:--->PageObjects(Packages)--->TestCases(Packages)--->Utilities(Packages)
#--->TestData(Folder)--->Configuration(Folder)--->Logs(Folder)--->Screenshots(Folder)
#--->Reports(Folder)--->Run.bat.

#Step3: Automating  Login Test Case
# Create LoginPage Object Class under "pageObjects"
# Create LoginTest under "testCases"
# Create conftest.py under "testCases"

#Step4: Capture screenshot on failure:
#Update Login Test with Screenshot under "testCases"

#Step5: Tead common values from .ini files.
#Add "config.ini" file in "Configuration" folder.
#Create "readProperties.py" utility file under utilities package to read common data.
#Replace hard coded values in Login test cases.

#Step6: Addings logs to test case:
# Add customLogger.py under utilities package.
# Add ;pgs tp Login test case.

#Step7: Run test on Desired Browser/Cross Browser/Parallel.
# Update contest.py with required Fixture which will accept command line argument(browser)
#Pass browser name as argument in command line.
#To run test on desired browser:
#pytest -s -v testCases/test_login.py --browser chrome
#pytest -s -v testCases/test_login.py --browser firefox

#To Run tests Parallel.
#pytest -s -v -n=3 testCases/test_login.py --browser chrome
#pytest -s -v- n=3 testCases/test_login.py --browser firefox

#Step8: Generation pytest HTML Reports:
#Update conftest.py with pytest hooks.
#To Generate HTML report run below command.
#pytest -s -v -n==3 --html=Reports/report.html testCases/test_login.py --browser chrome

#Step9: Automating Data Driven Test Case:
#Prepare test data in Excel sheet, place the excel file inside the TestData Folder.
#Create "ExcelUtils.py" utility class under utilities package.
#Create LoginDataDriven Test under TestCases.
#Run the test case.

#Step10: Adding new testCases.

#Step11: Grouping Tests:
#Grouping markers(Add ,markers to every test method)
#@pytest.mark.sanity
#@pytest.mark.regression
#Add Marker entries in pytest.ini file.
#pytest.ini
#.........
#[pytest]
#makers *
#sanity
#regression
#Select groups at run time:
#-m "sanity"
#-m "regression"
#-m "sanity and regression"
#-m "sanity or regression"
#Run Command:
#pytest -s -v -m "sanity" or "regression" -html=./Reports/report.html testCases/ --browser chrome

#Step 12: Run tests in Command Prompt & run.bat file.
#Create run.bat file

#pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser chrome
# Open cmmand prompt as Administrator and then run run.bat file.

#Step 13: Push the Code to Git & GitHub Repository.


