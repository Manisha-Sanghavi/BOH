Feature: Verify Functionalities for CSM user
#@smoke
  Scenario: [CSM-1] Verify that user with CSM role can not delete Customer from Info tab
    Given User is on BOH FPU homepage
    When User login with username "rashmi.chitnis@spurqlabs.com" and password "Chitnis@BOH22!"
    And User navigated to "Customer Management" page
    And User select customer
    And User tap on "INFO Tab" button
    Then User verifies "Delete Joe M" is not displayed on page

  Scenario: [CSM-2] Verify that user with CSM role can not delete Opportunity from the Info tab
    Given User is on BOH FPU homepage
    When User login with username "rashmi.chitnis@spurqlabs.com" and password "Chitnis@BOH22!"
    And User navigated to "Customer Management" page
    And User tap on "opportunities" button
    And User select opportunity
    Then User verifies "Delete opportunity #17" is not displayed on page

  Scenario:[CSM-3] Verify that user with CSM role, can not Delete RE which was created by other user
    Given user is on BOH FPU homepage
    When User login with username "rashmi.chitnis@spurqlabs.com" and password "Chitnis@BOH22!"
    And user navigated to "Customer Management" page
    And user taps on RE tab
    And user selects RE
    And User tap on "INFO" button
    Then User verifies "Delete Requirement Estimate" is not displayed on page


  Scenario: [CSM-4] Verify that user with CSM role, can delete RE created by its own account
    Given user is on BOH FPU homepage
    When User login with username "rashmi.chitnis@spurqlabs.com" and password "Chitnis@BOH22!"
    And user navigated to "Customer Management" page
    And user taps on RE tab
    And user taps on plus symbol
    And user taps on Add RE
    And user taps "MM/DD/YYYY"
    And user selects Estimated Order Date "06/06/2022"
    And user selects Opportunity "15" with name "Joe M"
    And user enter Pre-RE Footprint(Sq ft) as "70"
    And user selects Color "GREEN"
    And user taps "CREATE REQUIREMENTS ESTIMATE" to select
    And user tap on "INFO" button
    Then User verifies "Delete Requirements Estimate" is displayed on RE_Page
    And User taps on "Delete Requirements Estimate" option
    And User taps on "Yes" option

   Scenario: [CSM-5] Verify that for user with CSM role can not change Validate state of a RE to Active
     Given user is on BOH FPU homepage
    When User login with username "rashmi.chitnis@spurqlabs.com" and password "Chitnis@BOH22!"
    And user navigated to "Customer Management" page
    And user taps on RE tab
    And user taps on "Filter By" options
    And user taps on "Validate" option
    And user selects RE
    And user taps on "VALIDATE" option
    Then user verifies "Change RE State" is not displayed on page
