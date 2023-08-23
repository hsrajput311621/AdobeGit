*** Settings ***

Library    SeleniumLibrary


*** Variables ***

${url}  https://www.flipkart.com/
${browser}  Chrome


*** Test Cases ***
Validations
    open browser    ${url}  ${browser}
    wait until page contains    ${url}
    maximize browser window
    title should be    Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!
    ${input_tet}   set variable    xpath:/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input

    element should be enabled   ${input_tet}
    element should be visible   ${input_tet}
    sleep    2
    input text    xpath:/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input    9602408640
    sleep    2
    input text    xpath:/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input    Family@2022
    sleep   2
    click button    xpath:/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button
    sleep    10
    close browser

