*** Settings ***
Library    Selenium2Library
Variables    e2e_automation_testing/e2e_variable/variable/variable.py

*** Variables ***
${WEBSITE}      https://live.primedatacdp.com
${USERNAME}     //*[@id="username"]
${PASSWORD}     //*[@id="password"]
${BUTTON_LOGIN}     //*[@type="submit"]
${INPUT_USERNAME}    thang.tran@primedata.ai
${INPUT_PASSWORD}       Lunthse61727
${MENU_ITEM_PROFILE}    //*[@id="overlay"]//following::div[8]
${SEGMENT_ELEMENT}     //*[text()="Self-serve Segments"]
${CREATE_SEGMENT_ELEMENT}       //*[@id="Segments Overview"]//following::button[2]
${LIVE_SEGMENT}     Live Segment
${HISTORICAL_SEGMENT}     Historical Segment
${LIVE_AND_HISTORICAL_SEGMENT}     Live Segment with Historical Backfill
${BUTTON_START}         //*[@id="cp__cp-type-start"]

*** Keywords ***
Open to chrome
    [Documentation]    open to chrome webbrowser
    Open browser    ${WEBSITE}   chrome
    MAXIMIZE BROWSER WINDOW
    Sleep    2s

Login to the cdp web
    wait until element is visible       ${USERNAME}
    input text    ${USERNAME}  ${INPUT_USERNAME}
    wait until element is visible       ${PASSWORD}
    input text    ${PASSWORD}  ${INPUT_PASSWORD}
    wait until element is visible       ${BUTTON_LOGIN}
    click button    ${BUTTON_LOGIN}

Create live segment with historical
    wait until element is visible      ${MENU_ITEM_PROFILE}
    click element    ${MENU_ITEM_PROFILE}
    Sleep   2s
    click element    ${SEGMENT_ELEMENT}
    Sleep   2s
    mouse out       ${CREATE_SEGMENT_ELEMENT}
    click button    ${CREATE_SEGMENT_ELEMENT}
    Sleep   3s

Select the type segment with type is '${type_segment}'
#    ${list_sg} =    create list     ${LIVE_SEGMENT}     ${HISTORICAL_SEGMENT}       ${LIVE_AND_HISTORICAL_SEGMENT}
    run keyword if  '${type_segment}' == '${LIVE_SEGMENT}'          click element    //*[text()="${type_segment}"]
    ...         ELSE IF    '${type_segment}' == '${HISTORICAL_SEGMENT}'         click element    //*[text()="${type_segment}"]
    ...         ELSE IF    '${type_segment}' == '${LIVE_AND_HISTORICAL_SEGMENT}'       click element    //*[text()="${type_segment}"]
    click button    ${BUTTON_START}
    Sleep    10s