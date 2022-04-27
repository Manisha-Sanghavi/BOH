# Created by Rashmi at 21/04/2022
Feature: RE

  Scenario : Verify different options available in Sort By for RE Tab
    Given user is on BOH FPU homepage
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user taps on "Sort By" option
    Then user verifies following options are available:
       | Recent Activity | RE Date | Value | REID | Location | CSM | Status |

  Scenario : Verify user can sort REs in descending order of REID
    Given user is on BOH FPU homepage
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user taps on "upward arrow"
    Then user verifies REs diplayed are in descending order of REID

  Scenario : Verify user can sort REs in ascending order of REID
    Given user is on BOH FPU homepage
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user taps on "downward arrow"
    Then user verifies REs displayed are in descending order of REID

  Scenario : Verify different options available in Filter By for RE Tab
    Given user is on BOH FPU homepage
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user taps on "Filter By" option
    Then user verifies following options are available:
      | Current | All | Draft | Validate | Inactive | Active | Pending | Awarded | Complete |


  Scenario Outline : Verify user can filter REs by their states
    Given user is on BOH FPU homepage
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user taps on "Filter By" option
    And user select "<RE_Status>" from dropdown list
    Then user verifies REs with state "<RE_Status>" only are displayed
      Examples:
      | RE_Status |
      | Draft |
      | Validate |
 #   | Inactive | Active | Pending | Awarded | Complete |


  Scenario: Verify after tapping '+' symbol in RE tab, user can see Add Touchbase, Add Opportunity, Add RE and 'x' symbol
    Given user is on BOH FPU homepage
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user taps on '+' symbol
    Then user verifies following options are displayed:
    | Add Touchbase | Add Opportunity |Add RE | 'x' symbol |

  Scenario : Verify user can create RE successfully
    Given user is on BOH FPU homepage
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user taps on '+' symbol
    And user taps on Add RE
    And user selects Sales Rep "Chris Dykes"
    And user selects Estimated Order Date "21/05/2022"
    And user selects Opportunity Opp 48 . 14 BEB
    And user enter following details for selected Customer Info options
    |  Info  | RE Region | Customer Name | Customer Location |
    | Direct |   East    |    14 BEB     |   Aberdeen        |
    | Program| Anchor    | 2d SFAC       |  Australia        |
    And user enters the Primary Contact details as:
    | Rank or Title(Optional) | Contact First Name | Contact Last Name | Contact Email | Contact Phone |
    |   CW                    | David              | Coleman           | dc@email.com  | (020)741-5699 |
    And user enter following details for Metrics as:
    | Pre-RE Footprint(Sq ft) | Lift Capabilities | Color |
    |       70                |   25k Forklift    | Green |
    And user taps Create Requirements Estimate
    Then user verifies RE details page is displayed

  Scenario: Verify user can search existing RE by tapping on Search (Q) option
    Given user is on BOH FPU homepage
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user can see "Customer Management" page
    And user taps on RE tab
    And user taps on "search" symbol
    And user search for RE "772"
    And user selects "RE #772"
    Then user verifies "RE #772" details page are displayed

  Scenario: Verify the Headers and Tabs displayed in RE Details Page
    Given user is on BOH FPU homepage
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user selects first RE from REs list
    Then the following headers and tabs are displayed
    | RE ID | Status | Add Subtitle | Customer | Location | Info | Configs | Activity | Files |

  Scenario: Verify user can Add Subtitle to RE if its not already added
    Given user is on BOH FPU homepage
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user selects "RE #718"
    And user taps on "ADD SUBTITLE"
    And user enters subtitle "Requirements process"
    And user taps on "Save" option
    Then user verifies "Requirements process" subtitle is displayed

  Scenario: Verify user can Edit existing Subtitle successfully
    Given user is on BOH FPU homepage
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user selects "RE #666"
    And user taps on "pen" symbol given to edit subtitle
    And user edits subtitle as "Requirements changed"
    And user taps on "Save" option
    Then user verifies "Requirements changed" subtitle is displayed

  Scenario: Verify user can update details in Info section of RE successfully
    Given user is on BOH FPU homepage
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on "RE" tab
    And user selects "RE #864"
    And user taps on "Info" tab
    And user taps and selects following details as:
    |   Opportunity    |  Sales Rep  | Direct |
    |  Opp 47 . 14 BEB | Mike Gentry | West   |
    And user taps on Customer Contact
    And user edits the following details displayed :
    | First Name | Last Name | Contact Phone  |
    | Freddie    | Jackson   | (020) 992-2888 |
    And user taps on Add Another Date for Estimated Order Date
    And user selects date "24/05/2022"
    And user edits Metrics details as follows:
    | Pre-RE Footprint (sq ft) | Lift Capabilities | Default Color |
    |           79             |  HEMTT - LHS        |    Green    |
    And user taps on "Save Changes"
    Then user verifies the details in Info tab are updated

  Scenario: Verify user can Swap contact from Info tab in RE details page
    Given user is on BOH FPU homepage
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on "RE" tab
    And user selects "RE #825"
    And user taps on "Info" tab
    And user taps on "Swap Contact"
    And user selects first Contact displayed in the list
    And user taps on "Save Changes"
    Then user verifies swapped contact is displayed

  Scenario: Verify user can create Touchbase with Customer from Info tab of RE
    Given user is on BOH FPU homepage
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on "RE" tab
    And user selects "RE #826"
    And user taps on "Info" tab
    And user taps on "Touchbase with Matt"
    Then user verifies following details of Customer already filled to create Touchbase
    |    Customer        |         Location       |
    | 3-2d Av Regt(GSAB) |  Camp Humphreys, Korea |

  Scenario: Verify user can add multiple dates for Estimated Order Dates section in Info tab of RE details page
    Given user is on BOH FPU homepage
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on "RE" tab
    And user selects "RE #825"
    And user taps "Add Another Date"
    And user selects a date
    And user taps "Add Another Date"
    And user selects one more date
    And user taps on "Save Changes"
    Then user verifies dates are saved successfully

  Scenario: Verify user can remove dates from Estimated order date section in Info tab of RE details page
    Given user is on BOH FPU homepage
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
   And user is navigated to "Customer Management" page
    And user taps on "RE" tab
    And user selects "RE #825"
    And user taps "Add Another Date"
    And user selects a date
    And user taps on "Save Changes"
    And user taps on "x" symbol of last date under Estimated Order Dates
    And user taps on "Save Changes"
    Then user verifies that the date is removed successfully

  Scenario: Verify that for RE user can Create Configuration under Configured Systems successfully
    Given user is on BOH FPU homepage
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on "RE" tab
    And user selects "RE #826"
    And user taps on "+" symbol
    And user selects "Add Configuration"
    And user enters "New System"
    And user taps "Create" button
    And user taps on "find products"
    And user adds "Boh Cargo -6"
    And user navigates back with backward arrow
    Then user verifies "New System" is displayed

  Scenario: Verify that for RE user can Create Configuration under Loose Products successfully
    Given user is on BOH FPU homepage
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on "RE" tab
    And user selects "RE #826"
    And user taps on "+" symbol
    And user selects "Add Configuration"
    And user selects "Loose Products"
    And user enters "New Configuration"
    And user taps "Create" button
    And user taps on "find products"
    And user adds "Boh Cargo -6 Shelf"
    And user navigates back with backward arrow
    Then user verifies "New Configuration" is displayed


  Scenario : Verify that for RE user is able to see the details about Configured Systems and Loose Products
    Given user is on BOH FPU homepage
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on "RE" tab
    And user selects "RE #826"
    Then user verifies following details about number of Configured Systems and Loose Products are displayed
    | Configured Systems | Loose Products |
    |          3         |       4        |

  Scenario : Verify that after tapping on System under Configured Systems user is able to see the product details
    Given user is on BOH FPU homepage
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user selects "RE #826"
    And user taps on "System 1"
    Then user verifies following details about System are dispalyed
    | Containers | Container Accessories |


  Scenario : Verify that after tapping on Configuration under Loose Products user is able to see the product details
    Given user is on BOH FPU homepage
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user selects "RE #826"
    And user taps on "Configuration 1"
    Then user verifies following details about Configuration are dispalyed
    | Modules | Bulk Module #1 |

  Scenario: Verify that user can edit System name for Configured Systems of RE successfully
    Given user is on BOH FPU homepage
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on "RE" tab
    And user selects "RE #826"
#    And user taps on "+" symbol
#    And user selects "Add Configuration"
#    And user enters "New System"
#    And user taps "Create"
    And user taps on three dots "..." of first System in the list
    And user selects Edit system name
    And user "New System "
    And taps "Change" option
    Then user verifies "New System" name is displayed

  Scenario: Verify that user can duplicate System for Configured Systems of RE successfully
    Given user is on BOH FPU homepage
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on "RE" tab
    And user selects "RE #826"
#    And user taps on "+" symbol
  #  And selects "Add Configuration"
#    And user enters "New System"
#    And user taps "Create"
    And user taps on three dots "..." of first System in the list
    And user selects Duplicate System
    And taps "Add" button
    Then user verifies one duplicate of the system is created

  Scenario: Verify that user can delete System for Configured Systems of RE successfully
    Given user is on BOH FPU homepage
    And user creates one System under Configured Systems
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on "RE" tab
    And user selects "RE #826"
    And user taps on three dots "..." of New System
    And user selects Delete New System
    Then user verifies "New System" is deleted

  Scenario: Verify that user can edit Configuration name for Loose Products of RE successfully
    Given user is on BOH FPU homepage
    And user creates one Configuration under Loose Products
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on "RE" tab
    And user selects "RE #826"
    And user taps on three dots "..." of New Configuration
    And user selects Edit configuration name
    And user enters "New Config 1"
    And taps "Change" button
    Then user verifies "New Configuration" name is edited

  Scenario: Verify that user can duplicate Configuration for Loose Products of RE
    Given user is on BOH FPU homepage
    And user creates one Configuration under Loose Products
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on "RE" tab
    And user selects "RE #826"
    And user taps on three dots "..." of New Configuration
    And user selects Duplicate New Configuration
    And taps "Add" button
    Then user verifies one duplicate of the configuration is created

  Scenario: Verify that user can delete Configuration for Loose Products of RE
    Given user is on BOH FPU homepage
    And user creates one Configuration under Loose Products
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on "RE" tab
    And user selects "RE #826"
    And user taps on three dots "..." of New Configuration
    And user selects Delete New Configuration
    Then user verifies "New Configuration" is deleted

  Scenario: Verify that for any RE, the user is able to see various options for "+" symbol
    Given user is on BOH FPU homepage
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user selects "RE #793" (Draft Status RE)
    And user taps on "+" symbol
    Then following options are displayed:
     | Add Touchbase | Add Configuration | 'x' symbol |

  Scenario: Verify that user can change state of RE successfully
    Given user is on BOH FPU homepage
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user selects RE with any one of following status "RE #763"
    | Inactive | Active | Pending | Awarded | Complete |
    And user taps on Status of RE to select "Change RE Status"
    And user changes RE status to "Active"
    Then user verifies Status "Active" is displayed

  Scenario: Verify that after tapping Draft state of RE, three options are displayed as:Submit for Validation,Duplicate RE,Email NSN Worksheet
    Given user is on BOH FPU homepage
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user selects "RE #473"
    And user taps on RE status "Draft"
    Then user verifies following options are displayed:
    | Submit for Validation | Duplicate RE | Email NSN Worksheet |

  Scenario: Verify that after tapping Validate state of RE, three options are displayed as:Review and Validate,Duplicate RE,Email NSN Worksheet
    Given user is on BOH FPU homepage
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user selects "RE #779"
    And user taps on RE status "Validate"
    Then user verifies following options are displayed:
    | Review and Validate | Duplicate RE | Email NSN Worksheet |


  Scenario: Verify that user is able to Duplicate RE successfully
    Given user is on BOH FPU homepage
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user selects "RE #473"
    And user taps on RE status to select "Duplicate RE" option
    And user fills following details:
    | No. of Duplicates |   Opportunity   | Pre-RE Footprint(sq ft) |
    |      1            | Opp 48 . 14 BEB |         70              |
    And user taps on "Duplicate Requirements Estimation"
    Then user verifies that RE is duplicated

  Scenario: Verify that user is able to change Draft status of RE to Validate status
    Given user is on BOH FPU homepage
    And user creates "New RE" with Draft status
    And user creates "New System" under Configured Systems
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user selects "New RE"
    And user taps on RE status
    And user selects "Submit for Validation" option
    And user taps on "Next" button
    And user taps on "Submit for Validation" button
    Then user verifies Draft status of RE is changed to Validate

  Scenario: Verify that user is able to change Validate status of RE to Active status without sending email
    Given user is on BOH FPU homepage
    And user creates "New RE" with Draft status
    And user creates "New System" under Configured Systems
    And user changes Draft status of RE to Validate status
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user selects "New RE"
    And user taps on "Validate" status
    And user selects RE Date "7-05-2022"
    And user taps "Validate without sending" button
    Then user verifies Validate status of RE is changed to Active

  Scenario: Verify that user is able to change Validate status of RE to Active status and send email
    Given user is on BOH FPU homepage
    And user creates "New RE" with Draft status
    And user creates "New System" under Configured Systems
    And user changes Draft status of RE to Validate status
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user selects "New RE"
    And user taps on "Validate" status
    And user selects RE Date "7-05-2022"
    And user taps "Validate and Send" button
    Then user verifies Validate status of RE is changed to Active

  Scenario: Verify that for RE user is able to add a Recipient by entering an email to send NSN Worksheet
    Given user is on BOH FPU homepage
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user selects "RE #826"
    And user taps on Draft status
    And user selects "Email NSN Worksheet" option
    And user enters email "harish.ekal@spurqlabs.com"
    And user taps on "+" symbol
    Then user verifies email "harish.ekal@spurqlabs.com" is displayed under Added Recipient

  Scenario: Verify that for RE, user is able to send NSN Worksheet successfully
    Given user is on BOH FPU homepage
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user selects "RE #826"
    And user taps on Draft status
    And user selects "Email NSN Worksheet" option
    And user selects Chris Dykes
    And user taps "Send NSN" button
    Then user verifies RE page is displayed

  Scenario Outline: Verify that for RE in Info tab, user can select Confidence level to see the message displayed below
    Given user is on BOH FPU homepage
    And RE is in Active state
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user selects "RE #436"
    And user selects "<Confidence level>"
    Then user verifies "<message>" below "<Confidence level>" is displayed
      Examples:
    | Confidence level |                               message                         |
    |     10%          |           Providing Information-No Known Requirements         |
    |     25%          |         Customer Requested Survey-No Known Funding Source     |
    |     50%          |           Customer Wants It-CurrentlySeeking Funding          |
    |     75%          |  Customer Wants It-Funding Identified-Awaiting Authorization  |
    |     100%         | Customer has Provided Document Numbers or Confirmed Purchase  |

  Scenario: Verify that for RE in Info tab, user can change Confidence level successfully
    Given user is on BOH FPU homepage
    And RE is in Active state
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user selects "RE #436"
    And user selects "50%" Confidence level
    And user taps on "Save Changes" displayed
    Then user verifies under Confidence level, "50%" is displayed with message "Customer Wants It-CurrentlySeeking Funding"

  Scenario: Verify details added during RE Creation are displayed in Info Tab of that RE


  Scenario: Verify user can delete RE successfully
    Given user is on BOH FPU homepage
    And user creates "New RE"
    When user login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user selects "New RE"
    And user taps on Info tab
    And user taps on Delete Requirements Estimate
    And user taps on "Yes" button
    Then user verifies RE is not displayed in RE list
















