
Feature: Verify Functionalities for RE module
#@smoke
  Scenario: [RE-01] Verify different options available in Sort By for RE Tab
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    And user navigated to "Customer Management" page
    And user taps on RE tab
    And user taps on "Sort By" options
    Then user verifies following options are available for sort by
      |     Field       |
      | Recent Activity |
      |    RE Date      |
      |     Value       |
      |     REID        |
      |    Location     |
      |     CSM         |
      |     Status      |

  Scenario:[RE-02] Verify user can sort REs in descending order of REID
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    And user navigated to "Customer Management" page
    And user taps on RE tab
    Then user verifies REs displayed are in descending order of REID

  Scenario: [RE-03] Verify user can sort REs in ascending order of REID
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    And user navigated to "Customer Management" page
    And user taps on RE tab
    And user taps on "downward arrow"
    Then user verifies REs displayed are in ascending order of REID

  Scenario: [RE-04] Verify different options available in Filter By for RE Tab
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    And user navigated to "Customer Management" page
    And user taps on RE tab
    And user taps on "Filter By" options
    Then user verifies following options are available for filter by
      |     Field     |
      |    Current    |
      |      All      |
      |     Draft     |
      |    Validate   |
      |    Inactive   |
      |     Active    |
      |    Pending    |
      |    Awarded    |
      |    Complete   |


  Scenario Outline: [RE-05] Verify user can filter REs by their states
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    And user navigated to "Customer Management" page
    And user taps on RE tab
    And user taps on "Filter By" options
    And user select "<RE_Status>" from dropdown list
    Then user verifies REs with state "<RE_Status>" only are displayed
      Examples:
      | RE_Status |
      | Draft |
      | Validate |
    #| Inactive | Active | Pending | Awarded | Complete |


  Scenario: [RE-06] Verify after tapping '+' symbol in RE tab, user can see Add Touchbase, Add Opportunity and Add RE
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    And user navigated to "Customer Management" page
    And user taps on RE tab
    And user taps on plus symbol
    Then user verifies following options are displayed
                |      Field    |
                | Add Touchbase |
                |Add Opportunity|
                |    Add RE     |

  Scenario: [RE-07] Verify user can create RE successfully
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    And user navigated to "Customer Management" page
    And user taps on RE tab
    And user taps on plus symbol
    And user taps on Add RE
    And user selects Estimated Order Date "31/05/2022"
    And user enter following details for selected Customer Info options
         |       Field        |            Value            |
         |     RE Region      |             East            |
         |   Customer Name    |           Joe M             |
         | Customer Location  |          london             |
    And user enters the Primary Contact details as
          |        Field             |        Value         |
          | Rank or Title (optional) |          CW          |
          |   Contact First Name     |         David        |
          |    Contact Last Name     |        Coleman       |
          |       Contact Email      |      dc@email.com    |
          |        Contact Phone     |      (020)741-5699   |
    And user enter Pre-RE Footprint(Sq ft) as "70"
    And user enters Lift Capabilities as "5k Forklift"
    And user selects Color "TAN"
    And user taps Create Requirements Estimate
    Then user verifies RE details page is displayed

  Scenario: [RE-08] Verify user can search existing RE by tapping on Search (Q) option
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    And user navigated to "Customer Management" page
    And user taps on RE tab
    And user taps on "search" symbol
    And user enters "772" in search field
    And user selects RE# "772"
    Then user verifies searched RE details page is displayed
##
#  Scenario[RE-10]: Verify user can "Add Subtitle" to RE if its not already added
#    Given user is on BOH FPU homepage
#    When user login with "harish.ekal@spurqlabs.com" and "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on RE tab
#    And user selects RE# "878" from RE list
#    And user taps on "ADD SUBTITLE"
#    And user enters subtitle "Requirements process"
#    And user taps on "Save" option
#    Then user verifies "Requirements process" subtitle is displayed

  Scenario: [RE-11] Verify user can Edit existing Subtitle successfully
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    And user navigated to "Customer Management" page
    And user taps on RE tab
    And user selects RE# "864" from RE list
    And user edits subtitle as "Requirements changed"
    Then user verifies "Requirements changed" subtitle is displayed

#  Scenario[RE-12]: Verify user can update details in Info section of RE successfully
#    Given user is on BOH FPU homepage
#    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on "RE" tab
#    And user selects "RE #864"
#    And user taps on "Info" tab
#    And user taps and selects following details as:
#    |   Opportunity    |  Sales Rep  | Direct |
#    |  Opp 47 . 14 BEB | Mike Gentry | West   |
#    And user taps on Customer Contact
#    And user edits the following details displayed :
#    | First Name | Last Name | Contact Phone  |
#    | Fredrick    | Jackson   | (020) 992-2888 |
#    And user taps on Add Another Date for Estimated Order Date
#    And user selects date "24/05/2022"
#    And user edits Metrics details as follows:
#    | Pre-RE Footprint (sq ft) | Lift Capabilities | Default Color |
#    |           79             |  HEMTT - LHS        |    Green    |
#    And user taps on "Save Changes"
#    Then user verifies that following details in RE Info tab are displayed
#    | Opportunity   |Sales Rep  |Direct|First Name|Last Name|Contact Phone  |Pre-RE Footprint (sq ft)|Lift Capabilities|Default Color|
#    |Opp 47 . 14 BEB|Mike Gentry|West  |Fredrick  |Jackson  |(020) 992-2888 |          79            |  HEMTT - LHS    |    Green    |

#  Scenario: [RE-13] Verify user can Swap contact from Info tab in RE details page
#    Given user is on BOH FPU homepage
#    When user login with "harish.ekal@spurqlabs.com" and "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on RE tab
#    And user selects RE# "864" from RE list
#    And user taps on "Info" tab
#    And user taps on "Swap Contact"
#    And user selects first Contact displayed in the list
#    Then user verifies swapped contact is displayed
#    And user swap back the contacts

#  Scenario[RE-14]: Verify user can create Touchbase with Customer from Info tab of RE
#    Given user is on BOH FPU homepage
#    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on "RE" tab
#    And user selects "RE #826"
#    And user taps on "Info" tab
#    And user taps on "Touchbase with Matt"
#    Then user verifies following details of Customer already filled to create Touchbase
#    |    Customer        |         Location       |
#    | 3-2d Av Regt(GSAB) |  Camp Humphreys, Korea |
#
#  Scenario[RE-15]: Verify user can add multiple dates for Estimated Order Dates section in Info tab of RE details page
#    Given user is on BOH FPU homepage
#    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on "RE" tab
#    And user selects "RE #825"
#    And user taps "Add Another Date"
#    And user selects a date "25/03/2021
#    And user taps "Add Another Date"
#    And user selects one more date "15/03/2023
#    And user taps on "Save Changes"
#    Then user verifies dates are added successfully
#
#  Scenario[RE-16]: Verify user can remove dates from Estimated order date section in Info tab of RE details page
#    Given user is on BOH FPU homepage
#    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on "RE" tab
#    And user selects "RE #825"
#    And user taps "Add Another Date"
#    And user selects a date 25/03/2022
#    And user taps on "Save Changes"
#    And user taps on "x" symbol of last date under Estimated Order Dates
#    And user taps on "Save Changes"
#    Then user verifies that the date is removed successfully
#
#  Scenario[RE-17]: Verify that for RE user can Create Configuration under Configured Systems successfully
#    Given user is on BOH FPU homepage
#    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on "RE" tab
#    And user selects "RE #826"
#    And user taps on "+" symbol
#    And user selects "Add Configuration"
#    And user selects "Configured System"
#    And user enters Configuration System name as "test_System"
#    And user taps "Create" button
#    And user taps on "find products"
#    And user adds "Boh Cargo -6"
#    And user navigates back with backward arrow
#    Then user verifies "test_System" is displayed in Configured Systems list
#
#  Scenario[RE-18]: Verify that for RE user can Create Configuration under Loose Products successfully
#    Given user is on BOH FPU homepage
#    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on "RE" tab
#    And user selects "RE #826"
#    And user taps on "+" symbol
#    And user selects "Add Configuration"
#    And user selects "Loose Products"
#    And user enters "test_Configuration"
#    And user taps "Create" button
#    And user taps on "find products"
#    And user adds "Boh Cargo -6 Shelf"
#    And user navigates back with backward arrow
#    Then user verifies "test_Configuration" is displayed
#
#
#  Scenario[RE-19] : Verify that for RE user can see the details about Configured Systems and Loose Products
#    Given user is on BOH FPU homepage
#    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on "RE" tab
#    And user selects "RE #793"
#    Then user verifies following details about number of Configured Systems and Loose Products are displayed
#    | Configured Systems | Loose Products |
#    |          3         |       1        |
#
#  Scenario[RE-20]: Verify that after tapping on System under Configured Systems user can see the product details
#    Given user is on BOH FPU homepage
#    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on RE tab
#    And user selects "RE #826"
#    And user taps on "System 1"
#    Then user verifies following details about System are dispalyed
#    | Containers | Container Accessories |
#
#
#  Scenario[RE-21]: Verify that after tapping on Configuration under Loose Products user can see the product details
#    Given user is on BOH FPU homepage
#    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on RE tab
#    And user selects "RE #826"
#    And user taps on "Configuration 1"
#    Then user verifies following details about Configuration are dispalyed
#    | Modules | Bulk Module #1 |
#
#  Scenario[RE-22]: Verify that user can edit System name for Configured Systems of RE successfully
#    Given user is on BOH FPU homepage
#    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on "RE" tab
#    And user selects "RE #826"
#    And user taps on three dots "..." of first System in the list
#    And user selects Edit system name
#    And user enters Configured System name as "New_System "
#    And taps "Change" option
#    Then user verifies "New_System" name is displayed
#    And change "New_System" name to "System_1"
#
#  Scenario[RE-23]: Verify that user can duplicate System for Configured Systems of RE successfully
#    Given user is on BOH FPU homepage
#    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on "RE" tab
#    And user selects "RE #826"
#    And user taps on three dots "..." of first System in the list
#    And user selects Duplicate System
#    And taps "Add" button
#    Then user verifies one duplicate of the system is created
#
#  Scenario[RE-24]: Verify that user can delete System for Configured Systems of RE successfully
#    Given user is on BOH FPU homepage
#    And user creates one System under Configured Systems
#    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on "RE" tab
#    And user selects "RE #826"
#    And user taps on three dots "..." of New System
#    And user selects Delete New System
#    Then user verifies "New System" is deleted
#
#  Scenario[RE-25]: Verify that user can edit Configuration name for Loose Products of RE successfully
#    Given user is on BOH FPU homepage
#    And user creates one "New_Configuration" under Loose Products
#    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on "RE" tab
#    And user selects "RE #826"
#    And user taps on three dots "..." of "New_Configuration"
#    And user selects Edit configuration name
#    And user enters "New_Config_1"
#    And taps "Change" button
#    Then user verifies "New_Configuration" name is edited to "New_Config_1"
#
#  Scenario[RE-26]: Verify that user can duplicate Configuration for Loose Products of RE
#    Given user is on BOH FPU homepage
#    And user creates one "New_Configuration" under Loose Products
#    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on "RE" tab
#    And user selects "RE #826"
#    And user taps on three dots "..." of "New_Configuration"
#    And user selects Duplicate "New_Configuration"
#    And taps "Add" button
#    Then user verifies one duplicate of "New_Configuration" is created
#
#  Scenario[RE-27]: Verify that user can delete Configuration for Loose Products of RE
#    Given user is on BOH FPU homepage
#    And user creates one "New_Configuration" under Loose Products
#    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on "RE" tab
#    And user selects "RE #826"
#    And user taps on three dots "..." of "New_Configuration"
#    And user selects Delete New Configuration
#    Then user verifies ""New_Configuration"" is deleted
#
#  Scenario[RE-28]: Verify that for any RE, the user can see various options for "+" symbol
#    Given user is on BOH FPU homepage
#    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on RE tab
#    And user selects "RE #793" (Draft Status RE)
#    And user taps on "+" symbol
#    Then following options are displayed:
#     | Add Touchbase | Add Configuration | 'x' symbol |
#
#  Scenario[RE-29]: Verify that user can change state of RE successfully
#    Given user is on BOH FPU homepage
#    And status of "RE #763" is changed to Inactive
#    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on RE tab
#    And user selects "RE #763"
#    And user taps on  Inactive Status of RE
#    And user selects "Change RE Status"
#    And user changes RE status to "Active"
#    Then user verifies Status "Active" is displayed
#
#  Scenario[RE-30]: Verify that when user taps on "Draft" status of RE, three options are displayed as:Submit for Validation,Duplicate RE,Email NSN Worksheet
#    Given user is on BOH FPU homepage
#    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on RE tab
#    And user selects "RE #473"
#    And user taps on RE status "Draft"
#    Then user verifies following options are displayed:
#    | Submit for Validation | Duplicate RE | Email NSN Worksheet |
#
#  Scenario[RE-31]: Verify that when user taps on "Validate" status of RE, three options are displayed as:Review and Validate,Duplicate RE,Email NSN Worksheet
#    Given user is on BOH FPU homepage
#    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on RE tab
#    And user selects "RE #779"
#    And user taps on RE status "Validate"
#    Then user verifies following options are displayed:
#    | Review and Validate | Duplicate RE | Email NSN Worksheet |
#
#
##  Scenario[RE-32]: Verify that user can Duplicate RE successfully // There's no way to verify ( Defects 52 and 53
##  from defect sheet)
##    Given user is on BOH FPU homepage
##    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
##    And user is navigated to "Customer Management" page
##    And user taps on RE tab
##    And user selects "RE #473"
##    And user taps on RE status to select "Duplicate RE" option
##    And user fills following details:
##    | No. of Duplicates |   Opportunity   | Pre-RE Footprint(sq ft) |
##    |      1            | Opp 48 . 14 BEB |         70              |
##    And user taps on "Duplicate Requirements Estimation"
##    Then user verifies that RE is duplicated
#
#  Scenario[RE-33]: Verify that user can change "Draft" status of RE to "Validate" status
#    Given user is on BOH FPU homepage
#    And user creates "New RE" with Draft status
#    And user creates "New System" under Configured Systems
#    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on RE tab
#    And user selects "New RE"
#    And user taps on RE status
#    And user selects "Submit for Validation" option
#    And user taps on "Next" button
#    And user taps on "Submit for Validation" button
#    Then user verifies Draft status of RE is changed to Validate
#
#  Scenario[RE-34]: Verify that user can change "Validate" status of RE to "Active" status without sending email
#    Given user is on BOH FPU homepage
#    And user creates "New RE" with Draft status
#    And user creates "New System" under Configured Systems
#    And user changes Draft status of RE to Validate status
#    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on RE tab
#    And user selects "New RE"
#    And user taps on "Validate" status
#    And user selects RE Date "7-05-2022"
#    And user taps "Validate without sending" button
#    Then user verifies Validate status of RE is changed to Active
#
##  Scenario[RE-35]: Verify that user can change "Validate" status of RE to "Active" status and send email
##  // No way to verify if email is sent or not (Defect 54 in defect sheet )
##    Given user is on BOH FPU homepage
##    And user creates "New RE" with Draft status
##    And user creates "New System" under Configured Systems
##    And user changes Draft status of RE to Validate status
##    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
##    And user is navigated to "Customer Management" page
##    And user taps on RE tab
##    And user selects "New RE"
##    And user taps on "Validate" status
##    And user selects RE Date "7-05-2022"
##    And user taps "Validate and Send" button
##    Then user verifies Validate status of RE is changed to Active
#
#  Scenario[RE-36]: Verify that for RE user can add a Recipient by entering an email to send NSN Worksheet
#    Given user is on BOH FPU homepage
#    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on RE tab
#    And user selects "RE #826"
#    And user taps on Draft status
#    And user selects "Email NSN Worksheet" option
#    And user enters email "harish.ekal@spurqlabs.com"
#    And user taps on "+" symbol
#    Then user verifies email "harish.ekal@spurqlabs.com" is displayed under Added Recipient
#
#  Scenario[RE-37]: Verify that for RE, user can send NSN Worksheet successfully
#    Given user is on BOH FPU homepage
#    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on RE tab
#    And user selects "RE #826"
#    And user taps on Draft status
#    And user selects "Email NSN Worksheet" option
#    And user user enters email "harish.ekal@spurqlabs.com"
#    And user taps on "+" symbol
#    And user taps "Send NSN" button
#    Then user verifies RE page is displayed
#    # Mail is received with attached "NSN worksheet"  //if success msg is
#    #added then we can verify that msg (defect 54)
#
#  Scenario Outline[RE-38]: Verify that for RE in Info tab, user can select Confidence level to see their respective message displayed
#    Given user is on BOH FPU homepage
#    And RE is in Active state
#    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on RE tab
#    And user selects "RE #436"
#    And user selects "<Confidence level>"
#    Then user verifies for "<Confidence level>" respective "<Message>" is displayed is displayed
#      Examples:
#    | Confidence level |                               Message                         |
#    |     10%          |           Providing Information-No Known Requirements         |
#    |     25%          |         Customer Requested Survey-No Known Funding Source     |
#    |     50%          |           Customer Wants It-CurrentlySeeking Funding          |
#    |     75%          |  Customer Wants It-Funding Identified-Awaiting Authorization  |
#    |     100%         | Customer has Provided Document Numbers or Confirmed Purchase  |
#
#  Scenario[RE-39]: Verify that for RE in Info tab, user can change Confidence level successfully
#    Given user is on BOH FPU homepage
#    And RE is in Active state
#    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on RE tab
#    And user selects "RE #436"
#    And user selects "50%" Confidence level
#    And user taps on "Save Changes" displayed
#    Then user verifies under Confidence level, "50%" is displayed with message "Customer Wants It-Currently Seeking Funding"
#
#  Scenario[RE-40]: Verify details added during RE Creation are displayed in Info Tab of that RE
#    Given user is on BOH FPU homepage
#    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on RE tab
#    And user taps on "+" symbol
#    And user selects "Add RE"
#    And user fills the following details:
#    | Sales Rep |Estimated Order Date(optional)| Opportunity  |RE Program|Customer Name|Customer Location| Color |
#    | RT Riling |        07-05-2022            |Opp 56.newCust|  West    | newCust     |   29 palm       |  TAN  |
#    And user taps on Create Requirements Estimate
#    And user taps on Info tab
#    Then user verifies following details are displayed:
#    |  Opportunity   |  Sales Rep  | Direct | Estimated Order Dates | Default Color |
#    | Opportunity#56 | RT Riling   |  West  |        5/7/2022       |      TAN      |
#
#  Scenario[RE-41]: Verify user can delete RE successfully
#    Given user is on BOH FPU homepage
#    And user creates test_RE
#    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on RE tab
#    And user selects test_RE
#    And user taps on Info tab
#    And user taps on Delete Requirements Estimate
#    And user taps on "Yes" button
#    Then user verifies test_RE is not displayed in RE list
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
