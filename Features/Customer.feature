Feature: Mobile App Feature

  Scenario: [NAT-1] Verify the User can login successfully with valid credentials
    Given User is on boh fpu homepage
    When User enters username as "harish.ekal@spurqlabs.com"
    And User enters password as "Test123!BOH"
    And User taps on "Sign In" option
    Then User can see "Customer Management" page

  Scenario Outline: [NAT-2] Verify the User can not login with In-valid credentials
    Given User is on boh fpu homepage
    When User login with <username> and <password>
    Then User verifies "<message>"
    Examples:
      | username                  | password    | message                     |
      | harish.ekalspurqlabs.com  | Test123!BOH | Incorrect username/password |
      | harish.ekal@spurqlabs.com | test123     | Incorrect username/password |
      |                           |             | Incorrect username/password |

  Scenario: [NAT-3] Verify that the user is on the customer management page after signing in.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    Then Following options are displayed on homepage
      | Customer Management | Customers | REs       |
      | Opportunities       | Sort By   | Filter By |

  Scenario: [NAT-4] Verify after clicking on the profile, the user can see Sign-Out Option
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Adminastrator" option
    Then User can see "Sign Out" option

  Scenario: [NAT-5] Verify after clicking on profile, user can able to see Update Profile Picture option
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Adminastrator" option
    Then User can see "Update Profile Picture" option

  Scenario: [NAT-6] Verify after clicking on "Update Profile Picture", user should see two options 1) Take Picture 2) Upload File
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Adminastrator" option
    And User taps on "Update Profile Picture" option
    Then Following options are displayed
      | Take Picture |
      | Upload File  |

  Scenario: [NAT-7] Verify user can sign out after tapping on SignOut
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Adminastrator" option
    Then User taps on "Sign Out" option

  Scenario Outline: [NAT-8] Verify user can sort out customers by choosing different option [Date, CSM, Value, Name]
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Sort By" option
    And User select <sort by> option
    Then "Customers" list is displayed
    Examples:
      | sort by |
      | Date    |
      | CSM     |
      | Value   |
      | Name    |

  Scenario Outline: [NAT-9] Verify user can filter out customer by selecting different options [All, Active, Inactive]
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "filter By" option
    And User select <filter By> option
    Then "Customers" list is displayed
    Examples:
      | filter By |
      | All       |
      | Active    |
      | Inactive  |

  Scenario: [NAT-10] Verify user can search out exixting customer by tapping on Search (Q) option
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "search" option
    And User search for customer "newCust"
    Then "newCust" details are displayed


  Scenario: [NAT-11] Verify User can see Activity details after selecting existing customer
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    Then "abcd" details are displayed

  Scenario: [NAT-12] Verify User can able to see add Touchbase, Opportunity & RE by tapping on '+' symbol
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on '+' option
    Then Following options are displayed
      | Add Touchbase   |
      | Add Opportunity |
      | Add RE          |

 Scenario Outline: [NAT-13] Verify User can select different option from Direct in dropdown list
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on '+' option
    And User taps on "Add Touchbase" options
    Then User select <region> from list
    Examples:
      | region                  |
      | Americas (Excluding US) |
      | Central                 |
      | East                    |
      | Europe/Africa           |
      | Middle East             |
      | Pacific West            |

  Scenario: [NAT-14] Verify that the "forgot password" link works
    Given User is on boh fpu homepage
    When User taps on "Forgot Password" option
    Then User can see "Forgot your password?" page

  Scenario: [NAT-15] Verify user can able to see all details after tapping on Info tab [Sales Rep, Location, Contacts, Delete]
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User taps on "INFO" option
    Then Following options are displayed
      | Sales Rep |Location  |Contacts  |Delete    |

  Scenario: [NAT-16] Verify user can switch from Active to Inactive mode and vice versa.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And user can see "ACTIVITY" page
    And User taps on "ACTIVE" option
    And User can see "Change State" page
    Then User taps on "Set Customer to Inactive" option

  Scenario: [NAT-17] Verify user can check all options after tapping on the plus symbol in activity details [ Add Touchbase, Add contact, Add RE]
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User taps on '+' option
    Then Following options are displayed
      | Add Touchbase | Add contact|  Add RE |



  Scenario: [NAT-18] Verify that the user can edit location details and add a new location in the info tab of any customer.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User taps on "INFO" option
    And User taps on "location" option
    Then "new location" details are displayed

  Scenario: [NAT-19] Verify that users can see all details after tapping on contacts in the info tab of any customer.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User taps on "INFO" option
    And User taps on "Bradford Kasper" option
    Then Following options are displayed
      | hello@clearbluedesign.com |  | 000                     |
      | Edit Contact              |  | Touchbase with bradford |

  Scenario: [NAT-20] Verify that users can edit contact after tapping on contacts in the info tab of any customer
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User taps on "INFO" option
    And User taps on "Contact" option
    And User taps on "Edit Contact" option
    Then User can see "Edit Contact" page