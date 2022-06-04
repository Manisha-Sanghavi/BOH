Feature: Verify Functionalities for Customer module
#  @smoke
  Scenario: [Customer-1] Verify user can sort customers by Value option in ascending order
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    And User taps on "Sort By" option
    And User select "Value" option
    Then User verifies customer list is sorted in ascending order

    Scenario: [Customer-2] Verify user can sort customers by Date option in descending order
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    And User taps on "Sort By" option
    And User select "Value" option
    Then User verifies customer list is sorted in descending order

  Scenario: [Customer-3] Verify user can filter customer by Active option
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    And User taps on "filter By" option
    And User select "Active" option
    And User select customer
    Then User verifies Customer with only Active status are displayed

  Scenario: [Customer-4] Verify that the user can find an existing customer using the Search (Q) option.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    And User taps on "Search" option
    And User search for customer "Joe M"
    Then User verifies "Joe M" displayed on page

  Scenario: [Customer-5] Verify the Headers and Tabs displayed under Activity Tab
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    And User select customer
    And User navigated to "ACTIVITY Tab 2 of 3" page
    Then User verifies Customer details page with following information is displayed
      | Field               |
      | INFO Tab 1 of 3     |
      | ACTIVITY Tab 2 of 3 |
      | REs Tab 3 of 3      |
      | Note                |
      | Phone               |
      | Email               |
      | In-Person           |
      | Voicemail           |

  Scenario: [Customer-6] Verify after tapping '+' symbol in Customer tab, user can see Add Touchbase, Add Opportunity, Add RE and 'x' symbol
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    And User navigated to "customer management" page
    And User taps on "+" option
    Then User verifies following options are displayed on homepage
      | Field           |
      | Add Touchbase   |
      | Add Opportunity |
      | Add RE          |
      | X               |

  Scenario: [Customer-7] Verify user can switch from Active to Inactive mode
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    And User select customer
    And user taps on "ACTIVE" option
    And "Change State" popup is displayed
    And User taps on "Set Customer to Inactive" option
    And User verifies status changed to "INACTIVE"
    And user taps on "INACTIVE" option
    And User taps on "Set Customer to Active" option
    Then User verifies status changed to "ACTIVE"

#  Scenario: [Customer-8] Verify details added during customer creation are displayed in info tab of customer
#    Given User is on BOH FPU homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And User taps on "+" option
#    And User taps on "Add Touchbase" option
#    And User fills all required data into their respective field
#      | Field          | Value      |
#      | Customer       | John J     |
#      | Location       | 29 Palms   |
#      | Contact        | None       |
#      | Notes          | 9876543210 |
#      | Contact Method | Phone      |
#    And User taps on "CREATE TOUCHBASE" option
#    And User click on created touchbase
#    And User taps on "INFO Tab 1 of 3" option
#    And User verifies following options are displayed on Info tab
#      | Field              |
#      | Sales Rep Harish E |
#      | Locations          |
#      | Contacts           |
#      | no contacts        |
#    Then User taps on "Delete John J" option

#
  Scenario: [Customer-9] Verify that the customer summary shows all details.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    Then User verifies following summary of any customer displayed on homepage
      | Field      |
      | Joe M      |
      | london     |
      | Rashmi C   |
      | total REs  |
      | touchbases |
      | value      |
# No availability of independent locator
  Scenario: [Customer-10] Verify user can add a note successfully from Activity Tab in Customer Details page
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    And User select customer
    And User taps on "Post a message" option
    Then User verifies "Test" is displayed in Activity list.
#
#  Scenario: [Customer-11] Verify user can edit posted note from Activity tab.
#    Given User is on BOH FPU homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And User select customer
#    And User taps on "Post a message" option
#    And User selects "test1" to edit
#    And User edits to "test2"
#    Then User verifies note text is updated to "test2" in Activity list
#
#  Scenario: [Customer-12] Verify user can delete posted note text successfully
#    Given User is on BOH FPU homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And User select customer
#    And User selects "test2" to delete
#    And User taps on "delete" option
#    And "Delete Note" popup is displayed
#    Then User verifies "test2" is deleted successfully
#
#  Scenario Outline: [Customer-13] Verify user can create a Touchbase with selected contact option from Activity tab.
#    Given User is on BOH FPU homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And User selects "abcd" customer
#    And User navigated to "ACTIVITY" page
#    And User taps on "+" option
#    And User taps on "Add Touchbase" option
#    And User enter "<note>" in Note fields
#    And User taps on "<Contact Method>" option
#    And User taps on "Create Touchbase" option
#    Then User verifies "note" is displayed on page
#    Examples:
#    |Contact Method|note                     |
#    |Phone         |1234567890               |
#    |Email         |xyz@example.com          |
#    |In-Person     |text in In-Person        |
#    |Voicemail     |message through voicemail|
#
#  Scenario: [Customer-14] Verify that the user can delete created touchbase from Activity details
#    Given User is on BOH FPU homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And User select customer
#    And User navigated to "ACTIVITY Tab 2 of 3" page
#    And User taps on "+" option
#    And User taps on "Add Touchbase" option
#    And User enter "note" in Note fields
#    And User taps on "email" option
#    And User taps on "Create Touchbase" option
#    And User select recently created touchbase and delete it
#    Then User verifies "Touchbase" is deleted successfully


  Scenario: [Customer-15] Verify that user can update existing contact details in info tab of customer
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    And User select customer
    And User taps on "INFO Tab 1 of 3" option
    And User taps on "contact name" option
    And User taps on "Edit Contact" option
    And User enter "(123)456-7890" in contact phone
    And User taps on "Save Changes" option
    And User tap on "Back" button
    And User taps on "contact name" option
    Then User verifies "(123)456-7890" is displayed on page
    And User taps on "Edit Contact" option
    And User enter "(089)674-5131" in contact phone

  Scenario: [Customer-16] Verify that the push button functionality works.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    And User select customer
    And User taps on "INFO Tab 1 of 3" option
    And User taps on "contact name" option
    And User taps on "Edit Contact" option
    And User tap on "Push" button
    Then user verifies "Save Changes" is displayed on page
    And User tap on "Push" button

#    #    Low Priority.
  Scenario: [Customer-19] Verify that if there are no REs in the RE tab, then the user should able to see the message
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    And User select customer
    And User taps on "REs Tab 3 of 3" option
    Then user verifies "Tap the + to add the first RE" is displayed on page
