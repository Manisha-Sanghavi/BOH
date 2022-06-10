
Feature: Verify Functionalities for RE module
#@smoke
  Scenario: [RE-01] Verify different options available in Sort By for RE Tab
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    #And user navigated to "Customer Management" page
    And user taps on RE tab
    And user taps on "Sort By" options
    Then user verifies following fields are available
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
    #And user is navigated to "Customer Management" page
    And user taps on RE tab
    Then user verifies REs displayed are in "Descending" order of REID

  Scenario: [RE-03] Verify user can sort REs in ascending order of REID
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    #And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user taps on "downward arrow"
    Then user verifies REs displayed are in "Ascending" order of REID
#
  Scenario: [RE-04] Verify different options available in Filter By for RE Tab
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    #And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user taps on "Filter By" options
    Then user verifies following fields are available
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
    #And user is navigated to "Customer Management" page
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
    #And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user taps on plus symbol
    Then user verifies following options are displayed
                |      Field    |
                | Add Touchbase |
                |Add Opportunity|
                |    Add RE     |

  Scenario: [RE-07] Verify user can create RE without Opportunity
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    #And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user taps on plus symbol
    And user taps on Add RE
    And user taps "MM/DD/YYYY"
    And user selects Estimated Order Date "06/11/2022"
    And user enter following details for selected Customer Info options
         |       Field        |            Value            |
         |     RE Region      |             East            |
         |   Customer Name    |           Joe M             |
         | Customer Location  |          london             |
    And user enters the "New" Primary Contact details as
          |        Field             |        Value         |
          | Rank or Title (optional) |          CW          |
          |   Contact First Name     |         David        |
          |    Contact Last Name     |        Coleman       |
          |       Contact Email      |      dc@email.com    |
          |        Contact Phone     |      (020)741-5699   |
    And user enter Pre-RE Footprint(Sq ft) as "70"
    And user enters Lift Capabilities as "5k Forklift"
    And user selects Color "TAN"
    And user taps "CREATE REQUIREMENTS ESTIMATE" to select
    Then user verifies "RE" page is displayed with details "Joe M" and "london"
    And user deletes created RE by tapping "Delete Requirements Estimate"


  Scenario: [RE-08] Verify user can search existing RE by tapping on Search (Q) option
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    #And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user taps "Search" to select
    And user enters "943" in search field
    And user selects RE# "943" with location "london"
    Then user verifies searched RE# "943" details page is displayed

    Scenario: [RE-09] Verify user can create RE from Opportunity
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    #And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user taps on plus symbol
    And user taps on Add RE
    And user taps "MM/DD/YYYY"
    And user selects Estimated Order Date "07/05/2022"
    And user selects Opportunity "15" with name "Joe M"
    And user enter Pre-RE Footprint(Sq ft) as "70"
    And user selects Color "GREEN"
    And user taps "CREATE REQUIREMENTS ESTIMATE" to select
    Then user verifies RE details page is displayed with "Opportunity" number "Opp #15"
    And user deletes created RE by tapping "Delete Requirements Estimate"

  Scenario: [RE-10] Verify user can "Add Subtitle" to RE if its not already added
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    #And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user adds new RE as test_RE by tapping 'CREATE REQUIREMENTS ESTIMATE' with following customer info details
         |       Field        |            Value            |
         |     RE Region      |             East            |
         |   Customer Name    |           Joe M             |
         | Customer Location  |          london             |
    And user enters subtitle as "Requirements process"
    Then user verifies "Requirements process" subtitle is displayed
    And user deletes created RE by tapping "Delete Requirements Estimate"

  Scenario: [RE-11] Verify user can Edit existing Subtitle successfully
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    #And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user selects RE# "864" from RE list
    And user enters subtitle as "Requirements changed"
    Then user verifies "Requirements changed" subtitle is displayed
    And user enters subtitle as "Original RE"

  Scenario: [RE-12] Verify user can update contact details in Info section of RE successfully
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    #And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user "Search" RE# "943" with location "london" from RE list
    And user taps on "Info" tab
    And user edits the following details displayed
        |      Field       |       Value        |
        |   First Name     |    Fredrick        |
        |    Last Name     |     Jackson        |
        |   Contact Email  |    f.j@email.com   |
        |  Contact Phone   |    (020) 992-2888  |
    Then user verifies that following details in RE Info tab are displayed
          |      Field       |         Value         |
          |   Customer Name  |    Fredrick Jackson   |
          |   Contact Email  |    f.j@email.com      |
          |  Contact Phone   |   (020) 992-2888      |
    And user changes the contact details as 'Collin Woods' with 'c.w@email.com' and '0987654321'

#  Scenario: [RE-13] Verify user can update details as Opportunity, RE Date, Sale Rep, Direct and Metrics in Info section of RE successfully
#    Given user is on BOH FPU homepage
#    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on RE tab
#    And user selects RE# "864" from RE list
#    And user taps on "Info" tab
#    And user edits the following details are displayed
#        |         Field         |       Value        |
#        |      Opportunity      |    Opportunity #15 |
#        |       RE Date         |     9/23/2022      |
#        |      Sales Rep        |    Mike Gentry     |
#        |        Direct         |    Europe/Africa   |
#        |Pre-RE Footprint(sq ft)|          700       |
#        |     Default Color     |         GREEN      |
#    Then user verifies that following details in RE Info tab are displayed
#          |      Field       |         Value         |
#          |   Customer Name  |    Fredrick Jackson   |
#          |   Contact Email  |    f.j@email.com      |
#          |  Contact Phone   |   (020) 992-2888      |

  Scenario: [RE-14] Verify user can Swap contact from Info tab in RE details page
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    #And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user selects RE# "864" from RE list
    And user taps on "Info" tab
    And user taps "Swap Contact" to select
    And user selects Contact 'Todd Floyd (SSgt)' displayed in the list
    Then user verifies swapped contact 'Todd Floyd' is displayed
    And user swap back the contact to 'Collin Woods'

  Scenario: [RE-15] Verify user can create Touchbase with Customer from Info tab of RE
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    #And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user selects RE# "864" from RE list
    And user taps on "Info" tab
    And user taps on Touchbase with "Collin"
    Then user verifies Touchbase is created with 'Collin Woods' for RE# '864'
    And user "Delete Touchbase"
#
  Scenario: [RE-16] Verify user can add multiple dates for Estimated Order Dates section in Info tab of RE details page
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    #And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user selects RE# "864" from RE list
    And user taps on "Info" tab
    And user scrolls down
    And user taps "Add Another Date" to select
    And user selects Estimated Order Date "6/11/2022"
    And user taps "Add Another Date" to select
    And user selects Estimated Order Date "9/21/2022"
    And user taps "SAVE CHANGES"
    Then user verifies dates '6/11/2022' and '9/21/2022' are added successfully
    And user taps on x symbol to delete dates and "SAVE CHANGES"

  Scenario: [RE-17] Verify user can remove dates from Estimated order date section in Info tab of RE details page
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    #And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user selects RE# "864" from RE list
    And user taps on "Info" tab
    And user scrolls down
    And user taps "Add Another Date" to select
    And user selects Estimated Order Date "07/07/2022"
    And user taps "Add Another Date" to select
    And user selects Estimated Order Date "09/07/2022"
    And user taps "SAVE CHANGES"
    And user taps on x symbol to delete dates and "SAVE CHANGES"
    Then user verifies that the dates are removed successfully

  Scenario: [RE-18] Verify that for RE user can Create Configuration under Configured Systems successfully
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    #And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user "Search" RE# "940" with location "Amsterdam" from list
    And user taps on plus symbol to Add Configuration
    And user creates "Configuration System" name as "New System"
    And user adds product "Boh Cargo -6"
    Then user verifies "New System" is displayed in Configured Systems list
    And user taps on three dots "..." of "New Configuration" in the list
    And user taps "Delete New System"

  Scenario: [RE-19] Verify that for RE user can Create Configuration under Loose Products successfully
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    #And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user "Search" RE# "940" with location "Amsterdam" from list
    And user taps on plus symbol to Add Configuration
    And user creates "Loose Products" name as "New Configuration"
    And user adds product "Boh Cargo -6 Shelf"
    Then user verifies "New Configuration" is displayed in Loose Products list
    And user taps on three dots "..." of "New Configuration" in the list
    And user taps "Delete New Configuration"

  Scenario: [RE-20] Verify that for RE user can see the details about Configured Systems and Loose Products
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    #And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user "Search" RE# "942" with location "Aberdeen" from list
    Then user verifies number of Configured Systems: '3' and Loose Products: '1' are displayed as RE 'Products'

  Scenario: [RE-21] Verify that after tapping on System under Configured Systems user can see the product details
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    #And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user "Search" RE# "942" with location "Aberdeen" from list
    And user taps on System Product "New System"
    Then user verifies following details about Products are displayed
             |           Field            |
             |        Containers           |
             |   Container Accessories    |

  Scenario: [RE-22] Verify that after tapping on Configuration under Loose Products user can see the product details
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    #And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user "Search" RE# "942" with location "Aberdeen" from list
    And user taps on System Product "New Configuration"
    Then user verifies following details about Products are displayed
                |           Field            |
                |           Modules          |
                |   Module Accessories       |

  Scenario: [RE-23] Verify that user can edit System name for Configured Systems of RE successfully
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    #And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user "Search" RE# "943" with location "london" from RE list
    And user taps on plus symbol to Add Configuration
    And user creates "Configuration System" name as "New System"
    And user adds product "Boh Cargo -6"
    And user taps on three dots "..." of "New System" in the list
    And user changes Configured System name as "System 1"
    Then user verifies "System 1" name is displayed
    And user taps on three dots "..." of "New Configuration" in the list
    And user taps "Delete System 1"

  Scenario: [RE-24] Verify that user can duplicate System for Configured Systems of RE successfully
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    #And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user "Search" RE# "943" with location "london" from RE list
    And user taps on plus symbol to Add Configuration
    And user creates "Configuration System" name as "New System"
    And user adds product "Boh Cargo -6"
    And user taps on three dots "..." of "New System" in the list
    And user selects Duplicate "New System" to create "2" duplicates
    Then user verifies "2" "Duplicates" of the system is created for RE# "943" with location "london"
    And user deletes the "2" duplicates
    And user taps on three dots "..." of "New Configuration" in the list
    And user taps "Delete New System"

  Scenario: [RE-25] Verify that user can delete System for Configured Systems of RE successfully
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    #And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user "Search" RE# "943" with location "london" from RE list
    And user taps on plus symbol to Add Configuration
    And user creates "Configuration System" name as "New System"
    And user adds product "Boh Cargo -6"
    And user taps on three dots "..." of "New Configuration" in the list
    And user taps "Delete New System"
    Then user verifies "New System" is deleted with message "Tap the + to add the first system or loose product configuration"

  Scenario: [RE-26] Verify that user can edit Configuration name for Loose Products of RE successfully
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    #And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user "Search" RE# "943" with location "london" from RE list
    And user taps on plus symbol to Add Configuration
    And user creates "Loose Products" name as "New Configuration"
    And user adds product "Boh Cargo -6 Shelf"
    And user taps on three dots "..." of "New Configuration" in the list
    And user changes Configured System name as "Configuration 1"
    Then user verifies "Configuration 1" name is displayed
    And user taps on three dots "..." of "New Configuration" in the list
    And user taps "Delete Configuration 1"

  Scenario: [RE-27] Verify that user can duplicate Configuration for Loose Products of RE
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    #And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user "Search" RE# "943" with location "london" from RE list
    And user taps on plus symbol to Add Configuration
    And user creates "Loose Products" name as "New Configuration"
    And user adds product "Boh Cargo -6 Shelf"
    And user taps on three dots "..." of "New Configuration" in the list
    And user selects Duplicate "New Configuration" to create "3" duplicates
    Then user verifies "3" "Duplicates" of the system is created for RE# "943" with location "london"
    And user deletes the "3" duplicates
    And user taps on three dots "..." of "New Configuration" in the list
    And user taps "Delete New Configuration"

  Scenario: [RE-28] Verify that user can delete Configuration for Loose Products of RE
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    #And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user "Search" RE# "943" with location "london" from RE list
    And user taps on plus symbol to Add Configuration
    And user creates "Loose Products" name as "New Configuration"
    And user adds product "Boh Cargo -6 Shelf"
    And user taps on three dots "..." of "New Configuration" in the list
    And user taps "Delete New Configuration"
    Then user verifies "New System" is deleted with message "Tap the + to add the first system or loose product configuration"
#
  Scenario:[RE-29] Verify that for any RE, the user can see various options for "+" symbol
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    #And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user "Search" RE# "943" with location "london" from RE list
    And user taps on plus symbol to check the options
    Then user verifies following options are displayed
     |        Field      |
     |   Add Touchbase   |
     | Add Configuration |

  Scenario: [RE-30] Verify that user can change state of RE successfully
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    #And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user selects RE# 861
    And user taps "ACTIVE"
    And user taps "Change RE State"
    And user taps "Inactive"
    Then user verifies Status "INACTIVE" is displayed
    And user changes status "INACTIVE" to "Active" by tapping "Change RE State"

  Scenario: [RE-31] Verify that when user taps on "Draft" status of RE, three options are displayed as:Submit for Validation,Duplicate RE,Email NSN Worksheet
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    #And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user "Search" RE# "943" with location "london" from RE list
    And user taps "DRAFT"
    Then user verifies following alternatives are displayed
     |        Field              |
     |  Submit for Validation    |
     |     Duplicate RE          |
     |    Email NSN Worksheet    |

  Scenario: [RE-32] Verify that when user taps on "Validate" status of RE, three options are displayed as:Review and Validate,Duplicate RE,Email NSN Worksheet
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    #And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user "Search" RE# "876" with location "london" from RE list
    And user taps "VALIDATE"
    Then user verifies following alternatives are displayed
     |        Field              |
     |  Review and Validate      |
     |     Duplicate RE          |
     |    Email NSN Worksheet    |

#  Scenario[RE-33]: Verify that user can Duplicate RE successfully // There's no way to verify ( Defects 52 and 53
#  from defect sheet)
#    Given user is on BOH FPU homepage
#    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    #And user is navigated to "Customer Management" page
#    And user taps on RE tab
#    And user selects "RE #473"
#    And user taps on RE status to select "Duplicate RE" option
#    And user fills following details:
#    | No. of Duplicates |   Opportunity   | Pre-RE Footprint(sq ft) |
#    |      1            | Opp 48 . 14 BEB |         70              |
#    And user taps on "Duplicate Requirements Estimation"
#    Then user verifies that RE is duplicated
#
#  Scenario[RE-34]: Verify that user can change "Draft" status of RE to "Validate" status
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
#  Scenario[RE-35]: Verify that user can change "Validate" status of RE to "Active" status without sending email
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
#  Scenario[RE-36]: Verify that user can change "Validate" status of RE to "Active" status and send email
#  // No way to verify if email is sent or not (Defect 54 in defect sheet )
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
#    And user taps "Validate and Send" button
#    Then user verifies Validate status of RE is changed to Active

#  Scenario[RE-37]: Verify that for RE user can add a Recipient by entering an email to send NSN Worksheet
#    Given user is on BOH FPU homepage
#    When user login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And user is navigated to "Customer Management" page
#    And user taps on RE tab
#    And user selects RE# 861
#    And user taps "DRAFT"
#    And user taps "Email NSN Worksheet"
#    And user enters email "harish.ekal@spurqlabs.com"
#    And user taps on "+" symbol
#    Then user verifies email "harish.ekal@spurqlabs.com" is displayed under Added Recipient

#    Scenario[RE-38]: Verify that for RE, user can send NSN Worksheet successfully
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
#    # Mail is received with attached "NSN worksheet"
#    //if success msg is added then we can verify that msg (defect 54)

#  Scenario Outline[RE-39]: Verify that for RE in Info tab, user can select Confidence level to see their respective message displayed
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

 Scenario: [RE-40] Verify that for RE in Info tab, user can change Confidence level successfully
    Given user is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    And User navigated to "Customer Management" page
    And user taps on RE tab
    And user selects RE
    And User tap on "INFO" button
    And User taps on "50%" option
    And User taps on "SAVE CHANGES" option
#    Locators are not available
#    Then User verifies "Customer Wants it • Currently Seeking Funding" displayed on page
    And User came to previous position for re-usability

#  Scenario[RE-41]: Verify details added during RE Creation are displayed in Info Tab of that RE
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
#  Scenario[RE-42]: Verify user can delete RE successfully
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

