*** Settings ***
Library              BuiltIn
Library              SeleniumLibrary
Library              ExcelLibrary
Resource             Keywords.robot
*** Variables ***
${URL}               http://port-epmo-11jm1ipldsws5.mism8dq2g6.us-east-1.elasticbeanstalk.com/
${BROWSER}           Chrome
${DELAY}             2
${INPUT USERNAME}    username
${INPUT PASSWORD}    password
${VALID USERNAME}    PriyankaJ
${VALID PASSWORD}    1qaz!QAZ
*** Test Cases ***
Valid_Login
    Open Browser To Login Page and Maximise
    Input Text                                 ${INPUT USERNAME}                          ${VALID USERNAME}
    Input Text                                 ${INPUT PASSWORD}                          ${VALID PASSWORD}
    Set Selenium Speed                         2
    Click Button                               //div/div[2]/div/form/input[3] (edited)