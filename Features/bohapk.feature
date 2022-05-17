
Feature: Android BOH_FPU
  @smoke
#  Scenario: Verifying user can login successfully with valid credentials
#    Given Given User is on BOH FPU homepage
#    When User enters username as "harish.ekal@spurqlabs.com"
#    And User enters password as "Ekal@BOH123!"
#    And User taps on Sign In button
#    Then User verifies "Customer Management" page is displayed
##
#  Scenario: [BOH-3] Verify the Headers and Tabs displayed on Customer Management Page.
#    Given User is on BOH FPU homepage
#    When User login with "harish.ekal@spurqlabs.com" and "Ekal@BOH123!"
#    Then User verifies "Customer Management" "Customers" and REs are displayed on page
#
#  Scenario: [BOH-5] Verify user can update Profile picture from Profile menu
#    Given User is on BOH FPU homepage
#    When User login with "harish.ekal@spurqlabs.com" and "Ekal@BOH123!"
#    And User taps on "Administrator" option
#    And User taps on "Update Profile Picture" option
#    Then user verifies profile picture updated successfully
#
#  Scenario: [BOH-4] Verify user can sign out successfully from app
#    Given User is on BOH FPU homepage
#    When User login with "harish.ekal@spurqlabs.com" and "Ekal@BOH123!"
#    And User taps on "Administrator" option
#    And User taps on "Sign Out" button
#    Then User verifies "Homepage" is displayed
#
  Scenario : Verify different options available in Sort By for RE Tab
    Given user is on BOH FPU homepage
    When user login with "harish.ekal@spurqlabs.com" and "Ekal@BOH123!"
    And user is navigated to "Customer Management" page
    And user taps on RE tab
    And user taps on "Sort By" option
    Then user verifies option
     #  | Recent Activity | RE Date | Value | REID | Location | CSM | Status |
