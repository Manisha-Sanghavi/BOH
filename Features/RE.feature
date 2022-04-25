# Created by Rashmi at 21/04/2022
Feature: RE

  Scenario Outline : Verify User can sort REs with different drop down list options
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on RE tab
    And User taps on "Sort By" option
    And User select "<sort by>" option
    Then "REs" list is sorted and displayed
      Examples:
      | Recent Activity |
      | RE Date |
#      | Value | REID | Location | CSM | Status |

  Scenario : Verify User can sort REs in descending order of REID
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on RE tab
    And User taps on "Sort By" option
    And User select "REID" option
    Then User Verifies REs diplayed are in descending order of REID

  Scenario : Verify User can sort REs in ascending order of REID
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on RE tab
    And User taps on "Sort By" option
    And User select "REID" option
    And User taps on downward arrow next to "Sort By"
    Then User Verifies REs diplayed are in descending order of REID

  Scenario Outline : Verify User can filter REs by different filter options
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on RE tab
    And User taps on "Filter By" option
    And User select "<filter by>" option
    Then "REs" list is displayed
      Examples:
      | Current | All |


  Scenario Outline : Verify User can filter REs by their states
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on RE tab
    And User taps on "Filter By" option
    And User select "<filter by>" option
    Then "REs" list is displayed
      Examples:
    | Draft | Validate |
 #   | Inactive | Active | Pending | Awarded | Complete |


  Scenario: Verify various options are given after tapping '+' symbol
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on RE tab
    And User taps on '+' symbol
    Then Following options are displayed
    | Add Touchbase | Add Opportunity |Add RE | 'x' symbol |

  Scenario : Verify after tapping on Add RE, user is able to fill details and create RE successfully
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on RE tab
    And User taps on '+' symbol
    And User taps on Add RE
    And User selects Sales Rep "Chris Dykes"
    And User selects Estimated Order Date "21/05/2022"
    And User selects Opportunity Opp 48 . 14 BEB
    And User enter following details for selected Customer Info options
    |  Info  | RE Region | Customer Name | Customer Location |
    | Direct |   East    |    14 BEB     |   Aberdeen        |
    | Program| Anchor    | 2d SFAC       |  Australia        |
    And User enters the Primary Contact details as:
    | Rank or Title(Optional) | Contact First Name | Contact Last Name | Contact Email | Contact Phone |
    |   CW                    | David              | Coleman           | dc@email.com  | (020)741-5699 |
    And User enter following details for Metrics as:
    | Pre-RE Footprint(Sq ft) | Lift Capabilities | Color |
    |       70                |   25k Forklift    | Green |
    And User taps Create Requirements Estimate
    Then User verifies RE is created successfully

  Scenario: Verify user can search existing RE by tapping on Search (Q) option
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on RE tab
    And User taps on "search" symbol
    And User search for RE "772"
    And User selects RE displayed
    Then "RE #772" details are displayed

  Scenario: Verify the Headers and Tabs displayed in RE Details Page
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on RE tab
    And User selects "RE #718"
    Then the following headers and tabs are displayed
    | RE ID | Status | Add Subtitle | Customer | Location | Info | Configs | Activity | Files |

  Scenario: Verify User can Add Subtitle to RE if its not already added
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on RE tab
    And User selects "RE #718"
    And User taps on "ADD SUBTITLE"
    And User enter subtitle "Requirements process"
    And User taps on "Save"
    Then Subtitle is added

  Scenario: Verify User can Edit existing Subtitle successfully
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on RE tab
    And User selects "RE #666"
    And User taps on "pen" symbol given to edit subtitle
    And User edits subtitle as "Requirements changed"
    And User taps on "Save"
    Then  Subtitle is edited

  Scenario: Verify User can update details in Info section of RE
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on "RE" tab
    And User selects "RE #864"
    And User taps on "Info" tab
    And User taps and selects following details as:
    |   Opportunity    |  Sales Rep  | Direct |
    |  Opp 47 . 14 BEB | Mike Gentry | West   |
    And User taps on Customer Contact
    And User edits the following details displayed :
    | First Name | Last Name | Contact Phone  |
    | Freddie    | Jackson   | (020) 992-2888 |
    And User taps on Add Another Date for Estimated Order Date to select date "24/05/2022"
    And User edits Metrics details as follows:
    | Pre-RE Footprint (sq ft) | Lift Capabilities | Default Color |
    |           79             |  HEMTT - LHS        |    Green    |
    And User taps on Save Changes
    Then the details in Info tab are updated

  Scenario: Verify user can Swap contact from Info tab in RE details page
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on "RE" tab
    And User selects "RE #825"
    And User taps on "Info" tab
    And User taps on "Swap Contact"
    And User selects first Contact displayed in the list
    And User taps on Save Changes
    Then User is able to swap contact

  Scenario: Verify user can create touchbase with Customer from Info tab of RE
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on "RE" tab
    And User selects "RE #826"
    And User taps on "Info" tab
    And User taps on "Touchbase with Matt"
    Then User is able to see details of Customer already filled to create Touchbase

  Scenario: Verify User can add multiple dates in Estimated Order Dates section in Info tab in RE details page
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on "RE" tab
    And User selects "RE #825"
    And User taps "Add Another Date" and selects a date
    And User taps "Add Another Date" and selects one more date
    And User taps on "Save Changes"
    Then dates are saved successfully

  Scenario: Verify user can remove dates from Estimated order date section in Info tab in RE details page
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on "RE" tab
    And User selects "RE #825"
    And User taps "Add Another Date" and selects a date
    And User taps on "Save Changes"
    And User taps on "x" symbol of last date under Estimated Order Dates
    And User taps on "Save Changes"
    Then date is removed successfully


  Scenario : Verify that user is able to see the details about Configured Systems and Loose Products
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on "RE" tab
    And User selects "RE #826"
    Then User validates details about Configured Systems and Loose Products is displayed

  Scenario : Verify that after tapping on Configured Systems user can see the details about System
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on RE tab
    And User selects "RE #826"
    And User taps on "System 1"
    Then User validates details about System is dispalyed


  Scenario : Verify that after tapping on Loose Products user can see the details about Configuration
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on RE tab
    And User selects "RE #826"
    And User taps on "Configuration 1"
    Then User validates details about Configuration is dispalyed

  Scenario: Verify that for Configured Systems user can perform various Actions
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on "RE" tab
    And User selects "RE #826"
    And User taps on three dots "..." of "System 1"
    Then User validates following actions:
      |Edit System name|Duplicate System|Delete System|

  Scenario: Verify that User can edit and save System name for Configured Systems of RE
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on "RE" tab
    And User selects "RE #826"
    And User taps on "+" symbol and selects "Add Configuration"
    And User enters "New System"
    And User taps "Create"
    And User taps on three dots "..." of New System
    And User selects Edit system name
    And User "New System 1"
    And taps "Change"
    Then System name is edited

  Scenario: Verify that User can duplicate System for Configured Systems of RE
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on "RE" tab
    And User selects "RE #826"
    And User taps on "+" symbol and selects "Add Configuration"
    And User enters "New System"
    And User taps "Create"
    And User taps on three dots "..." of New System
    And User selects Duplicate New System
    And taps "Add"
    Then One duplicate of the system is created

  Scenario: Verify that User can delete System for Configured Systems of RE
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on "RE" tab
    And User selects "RE #826"
    And User taps on "+" symbol and selects "Add Configuration"
    And User enters "New System"
    And User taps "Create"
    And User taps on three dots "..." of New System
    And User selects Delete New System
    Then New System is deleted


  Scenario: Verify that for Loose Products user can perform various Actions
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on RE tab
    And User selects "RE #824"
    And User taps on three dots ... for Configuration 1
    Then User validates following actions
      |Edit Configuration name|Duplicate Configuration|Delete Configuration|

  Scenario: Verify that User can edit and save Configuration name for Loose Products of RE
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on "RE" tab
    And User selects "RE #826"
    And User taps on "+" symbol and selects "Add Configuration"
    And User selects "Loose Products"
    And User enters "New Configuration"
    And User taps "Create"
    And User taps on three dots "..." of New Configuration
    And User selects Edit configuration name
    And User enters "New Config 1"
    And taps "Change"
    Then Configuration name is edited

  Scenario: Verify that User can duplicate Configuration for Loose Products of RE
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on "RE" tab
    And User selects "RE #826"
    And User taps on "+" symbol and selects "Add Configuration"
    And User selects "Loose Products"
    And User enters "New Configuration"
    And User taps "Create"
    And User taps on three dots "..." of New Configuration
    And User selects Duplicate New Configuration
    And taps "Add"
    Then One duplicate of the configuration is created

  Scenario: Verify that User can delete Configuration for Loose Products of RE
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on "RE" tab
    And User selects "RE #826"
    And User taps on "+" symbol and selects "Add Configuration"
    And User selects "Loose Products"
    And User enters "New Configuration"
    And User taps "Create"
    And User taps on three dots "..." of New Configuration
    And User selects Delete New Configuration
    Then New Configuration is deleted

  Scenario: Verify that for any RE, the user is able to see various options for "+" symbol
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on RE tab
    And User selects "RE #793" (Draft Status RE)
    And User taps on "+" symbol
    Then following options are displayed:
     | Add Touchbase | Add Configuration | 'x' symbol |

  Scenario: Verify user is able to create Configured System with System containing Container and different products
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on RE tab
    And User selects "RE #793" (Draft Status RE)
    And User taps on "+" symbol
    And User selects "Add Configuration"
    And User enters "New System"
    And User taps "Create"
    And User taps on "find products"
    And User taps "+" symbol for "BOH Cargo-6"
    Then New System is created with BOH Cargo-6 container

  Scenario: Verify user is able to create Loose Products with Configuration containing accessories
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on RE tab
    And User selects "RE #793" (Draft Status RE)
    And User taps on "+" symbol
    And User selects "Add Configuration"
    And User selects "Loose Products"
    And User enters "New Configuration"
    And User taps "Create"
    And User taps on "find products"
    And User taps "+" symbol for "BOH Cargo-6 Shelf"
    Then New Configuration is created with BOH Cargo-6 Shelf accessory

  Scenario: Verify that user can change state of RE successfully
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on RE tab
    And User selects RE with any one of following status "RE #763"
    | Inactive | Active | Pending | Awarded | Complete |
    And User taps on Status of RE to select "Change RE Status"
    And User changes RE status to "Active"
    Then User validates Status is changed

  Scenario: Verify that RE in Draft state have three options as:Submit for Validation,Duplicate RE,Email NSN Worksheet
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on RE tab
    And User selects "RE #473"
    And User taps on RE status "Draft"
    Then following options are displayed
    | Submit for Validation | Duplicate RE | Email NSN Worksheet |

  Scenario: Verify that RE in Validate state have three options as:Review and Validate,Duplicate RE,Email NSN Worksheet
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on RE tab
    And User selects "RE #779"
    And User taps on RE status "Validate"
    Then following options are displayed
    | Review and Validate | Duplicate RE | Email NSN Worksheet |


  Scenario: Verify that user is able to fill the details for Duplicate RE and RE is duplicated successfully
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on RE tab
    And User selects "RE #473"
    And User taps on RE status to select "Duplicate RE" option
    And User fills following details:
    | No. of Duplicates |   Opportunity   | Pre-RE Footprint(sq ft) |
    |      1            | Opp 48 . 14 BEB |         70              |
    And User taps on "Duplicate Requirements Estimation"
    Then User validates that RE is duplicated

  Scenario: Verify that User is able to submit RE in Draft status for validation
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on RE tab
    And User taps on "+" symbol to select "Add RE"
    And User fill the details to create RE with Draft status
    And User selects this RE
    And User taps on "+" symbol and selects "Add Configuration"
    And User creates Configured System with adding products as containers
    And User taps on RE status to select "Submit for Validation" option
    And User taps on "Next" button
    And User taps on "Submit for Validation"
    Then Draft status of RE is changed to Validate

  Scenario: Verify that User is able to submit RE in Validate status for review and validation
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on RE tab
    And User taps on "+" symbol to select "Add RE"
    And User fill the details to create RE with Draft status
    And User selects this RE
    And User taps on "+" symbol and selects "Add Configuration"
    And User creates Configured System with adding products as containers
    And User taps on RE status to select "Submit for Validation" option
    And User taps on "Next" button
    And User taps on "Submit for Validation"
    And User taps on "Validate" status
    And User selects RE Date "7-05-2022"
    And User taps Validate without sending
    Then Validate status of RE is changed to Active







