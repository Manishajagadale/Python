***Settings***
Library       SeleniumLibrary
Variables     locators.py

***Variables***
${Browser}    Chrome
${URL}        http://www.gmail.com
${id}         identifierId
${idvalue}    manishajagadale12@gmail.com
${DELAY}      2
***Test cases ***
LoginGmail
    Open Browser     ${URL}                        ${Browser}
    Input text       ${id}                         ${idvalue}
    Click element    //span[contains(.,'Next')]

    Input Text       name=password                 9623482323