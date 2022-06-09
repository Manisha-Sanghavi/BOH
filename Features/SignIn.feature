Feature: Verify Functionalities for Sigin, Sign out and Home Page

  Scenario: [BOH-1] Verify the User can login successfully with valid credentials
    Given User is on BOH FPU homepage
    When User enters username as "harish.ekal@spurqlabs.com"
    And User enters password as "Ekal@BOH123!"
    And User taps on Sign In button
    Then User verifies "Customer Management" page is displayed

  Scenario Outline: [BOH-2] Verify the User can not login with In-valid credentials
    Given User is on BOH FPU homepage
    When User login with "<username>" and "<password>" for validation
    Then User verifies "<message>" is displayed on page
    Examples:
      | username                  | password    | message                     |
      | harish.ekalspurqlabs.com  | Test123!BOH | Incorrect username/password |
      | harish.ekal@spurqlabs.com | test123     | Incorrect username/password |
#      |                           |             | Incorrect username/password |
      | harish.ekal               | test123     | Incorrect username/password |
#      |harish.ekal@spurqlabs.com  |             | Incorrect username/password |

  Scenario: [BOH-3] Verify the Headers and Tabs displayed on Customer Management Page.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    Then User verifies following options are displayed on page
      | Field                    |
      | Customer Management      |
      | Customers Tab 1 of 3     |
      | REs Tab 2 of 3           |
      | Opportunities Tab 3 of 3 |

#  Scenario: [BOH-4] Verify user can update Profile picture from Profile menu
#    Given User is on BOH FPU homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And User taps on "Adminastrator" option
#    And User taps on "Update Profile Picture" option
#    Then user verifies profile picture updated successfully
#
  Scenario: [BOH-5] Verify user can sign out successfully from app
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    And User taps on "Administrator" option
    And User taps on Sign Out button
    Then User verifies "Homepage" is displayed

   Scenario: [BOH-6] Verify that the "forgot password" link works
    Given User is on BOH FPU homepage
    When User taps on "forgot password" option
    And User navigated to "Forgot your password?" page
    And User enters email "harish.ekal@spurqlabs.com" in type your BOH email field
    And User taps on "SEND" option
    Then User verifies message "A recovery email has been sent to your account" is displayed

# Scenario: [BOH-7] Verify that the user can create a new touchbase successfully.
#  Given User is on BOH FPU homepage
#  When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#  And User taps on "+" option
#  And User taps on "Add Touchbase" option
#  And User fills all required data into their respective field
#    | Field          | Value      |
#    | Customer       | John J     |
#    | Location       | 29 Palms   |
#    | Contact        | None       |
#    | Notes          | 9876543210 |
#    | Contact Method | Phone      |
#  And User taps on "CREATE TOUCHBASE" option
#  Then user verifies "John J" is displayed on page
#
#  Scenario: [BOH-8] Verify user can delete Customer from Touchbase info tab
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
#    And User taps on "Delete John J" option
#    Then user verifies "All associated data will be permanently removed" is displayed on page

#  Scenario: [BOH-9] Verify that selecting "Remember me", user should able to see security page after closing an application.
#    Given User is on BOH FPU homepage
#    When User enters username as "harish.ekal@spurqlabs.com"
#    And User enters password as "Ekal@BOH123!"
#    And User taps on "Remember Me" option
#    And User taps on Sign In button
#    And User close the application & re-open it
#    Then User verifies "Welcome back" is displayed on page
