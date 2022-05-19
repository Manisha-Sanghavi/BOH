Feature: Verify Functionalities for Customer module
  @smoke
  Scenario: [Customer-1] Verify user can sort customers by Date option in ascending order
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    And User taps on "Sort By" option
    And User select "Date" option
    Then User verifies customer list is sorted in ascending order

    Scenario: [Customer-2] Verify user can sort customers by Date option in descending order
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Sort By" option
    And User select "Date" option
    Then User verifies customer list is sorted in descending order

  Scenario: [Customer-3] Verify user can filter customer by Active option
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "filter By" option
    And User select "Active" option
    Then User verifies Customer with only Active status are displayed

  Scenario: [Customer-4] Verify that the user can find an existing customer using the Search (Q) option.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "search" option
    And User search for customer "newCust"
    Then User verifies "newCust" displyed on page


  Scenario: [Customer-5] Verify the Headers and Tabs displayed under Activity Tab
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User selects "abcd" customer
    And User navigeated to "Activity" page
    Then User verifies Customer details page with following information is displayed
      | INFO | ACTIVITY | REs | Note | Phone | Email | In-Person | Voicemail |

  Scenario: [Customer-6] Verify after tapping '+' symbol in Customer tab, user can see Add Touchbase, Add Opportunity, Add RE and 'x' symbol
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User is navigated to "customer management" page
    And User taps on '+' option
    Then User verifies following options are displayed
      | Add Touchbase | Add Opportunity | Add RE |X|


  Scenario: [Customer-7] Verify user can switch from Active to Inactive mode
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User selects "abcd" customer
    And user navigated to "abcd" page
    And "Change State" popup is displayed
    And User taps on "Set Customer to Inactive" option
    And User verifies status changed to “Inactive”
    And User taps on "Set Customer to Active" option
    Then User verifies status changed to “Active”

  Scenario: [Customer-8] Verify details added during customer creation are displayed in info tab of customer
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "+" option
    And User taps on "Add Touchbase" option
    And User fills all required data into their respective field
        |Customer          |Location         |Direct/Program|Contact      |Existing/New/None|Rank or Title (optional)|                   |
        |Contact First Name|Contact Last Name|Contact Email |Contact Phone|Date of Contacts |Note                    |Contact Method     |
    And User taps on "Create Touchbase" option
    Then User verifies following options are displayed
      |Sales Rep  | Ron P         |                    |                   |              |
      |Location   |29 palm        |Arlington, VA       |Florida            |JBER, AK      |
      |Contacts   |Bradford Kasper|Jesus Amsdell       |Behanzin Luzunaris |Gretta Sevilla|

  Scenario: [Customer-9] Verify that the customer summary shows all details.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    Then User verifies following summary of "abcd" customer displayed on page
      | abcd          | Ron P    |
      | 29 Palm       | Active   |
      | Arlington, VA | Validate |
      | Florida       | Active   |
      | JBER, AK      | Active   |

  Scenario: [Customer-10] Verify user can add a note successfully from Activity Tab in Customer Details page
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User enter "Test note" in input field at bottom of the page
    And User taps on "Post" option
    Then User verifies "Test note" is displayed in Activity list.

  Scenario: [Customer-11] Verify user can edit posted note from Activity tab.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User enters "test1" in post a message field and send it
    And User selects "test1" to edit
    And User edits to "test2"
    Then USer verifies note text is updated to "test2" in Activity list

  Scenario: [Customer-12] Verify user can delete posted note text successfully
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User selects "abcd" customer
    And User selects "test2" to delete
    And User taps on "delete" option
    And "Delete Note" popup is displayed
    Then User verfies "test2" is deleted successfully

  Scenario Outline: [Customer-13] Verify user can create a Touchbase with selected contact option from Activity tab.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User selects "abcd" customer
    And User navigated to "ACTIVITY" page
    And User taps on "+" option
    And User taps on "Add Touchbase" option
    And User enter "<note>" in Note fields
    And User taps on "<Contact Method>" option
    And User taps on "Create Touchbase" option
    Then User verifies "note" is displayed on page
    Examples:
    |Contact Method|note                     |
    |Phone         |1234567890               |
    |Email         |xyz@example.com          |
    |In-Person     |text in In-Person        |
    |Voicemail     |message through voicemail|

  Scenario: [Customer-14] Verify that the user can delete created touchbase from Activity details
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User selects "abcd" customer
    And User navigated to "Activity" page
    And User taps on "+" option
    And User taps on "Add Touchbase" option
    And User enter "note" in Note fields
    And User taps on "email" option
    And User taps on "Create Touchbase" option
    And User select recently created touchbase and delete it
    Then User verifies "Touchbase" is deleted successfully


  Scenario: [Customer-15] Verify that user can update existing contact details in info tab of customer
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User selects "abcd" customer
    And User taps on "INFO" option
    And User taps on "Bradford Kasper" option
    And User taps on "Edit Contact" option
    And User enter "1234567890" in contct phone
    And User taps on "Save Changes" option
    And User taps on "Back" option
    And User taps on "Edit Contact" option
    Then User verifies "1234567890" is displayed on page

  Scenario: [Customer-16] Verify that the push button functionality works.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User selects "abcd" customer
    And User taps on "INFO" option
    And User taps on "Jesus Amsdell" option
    And User taps on "Edit Contact" option
    And User navigated to "Edit Contact" page
    And User taps on "Push" button
    Then user verifies "Save Changes" is displayed on page


  Scenario: [Customer-17] Verify User can sort customers in descending order
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User navigated to "Customer Management" page
    And User taps on "Upside arrow" option
    Then User verifies "customer list" is displayed in descending order

  Scenario: [Customer-18] Verify User can sort customers in ascending order
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User navigated to "Customer Management" page
    And User taps on "downside arrow" option
    Then User verifies "customer list" is displayed in ascending order


    #    Low Priority.
  Scenario: [Customer-19] Verify that if there are no REs in the RE tab, then the user should able to see the message
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User selects "abcd" customer
    And User taps on "RE" option
    Then user verifies "Tap the + to add the first RE" is displayed on page
