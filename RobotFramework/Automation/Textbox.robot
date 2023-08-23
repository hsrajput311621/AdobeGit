*** Settings ***

Library    SeleniumLibrary


*** Variables ***

${url}  https://www.google.com/
${browser}  Chrome

*** Test Cases ***
TextBoxes
    open browser    ${url}  ${browser}
    maximize browser window
    sleep    2
    input text    xpath:/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input      Amazon
    click button    xpath:/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]
    clear element text  xpath://input[@aria-label='Search']
    sleep    2
    input text    xpath://input[@aria-label='Search']   flipkart
    click button    xpath://body/div[@id='searchform']/div[2]/form[1]/div[1]/div[1]/div[2]/button[1]
    sleep    3
    close browser

*** Keywords ***


