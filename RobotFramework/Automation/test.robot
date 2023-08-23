# This is the test file for the RobotFramework#
# Settings contain all the library to create the test cases for Automation framework#

*** Settings ***

Library     SeleniumLibrary


*** Variable ***

${url}		https://www.google.com/
${browser}  Chrome

*** Test Cases ***
Google
	#open browser    		${url}		${browser}
	loginToApplication
	#maximize browser window
	#sleep    3
	#close browser

*** Keywords ***
loginToApplication
    open browser    		${url}		${browser}
	maximize browser window
	sleep    3
	close browser