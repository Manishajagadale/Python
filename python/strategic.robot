***Settings***
Library       SeleniumLibrary
***Variables***
${Browser}    Chrome
${URL}        http://port-epmo-11jm1ipldsws5.mism8dq2g6.us-east-1.elasticbeanstalk.com/
***Test cases ***
strateg-eit login
    Open Browser    ${URL}           ${Browser}
    Input Text      name=username    manishaj
    input Text      name=password    Manishajagadale@13
