Feature: Verify Feature: Verify Functionalities for Opportunity module
#@smoke
  Scenario: [Opportunity-1] Verify that the user can create a new opportunity successfully.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    And User taps on "+" option
    And User taps on "Add Opportunity" option
    And User fills all required data into their respective field for opportunity
      | Field           |
      | Affiliation     |
      | Customer        |
      | Location        |
      | BOH Role        |
      | Win Probability |
      | Value Breakdown |
    And User taps on "CREATE OPPORTUNITY" option
    And User tap on "opportunities" button
    Then user verifies "Est. Order Date 6/2022" is displayed on page
    And User tap on "opportunities" button
    And User select opportunity
    And User taps on "Delete Opportunity" option
#
  Scenario: [Opportunity-2]Verify that the user can see the opportunities summary part displayed on the page.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    And User tap on "opportunities" button
    Then User verifies following options are displayed in opportunity details
      | Field           |
      | Opportunity #17 |
      | Joe M           |
      | london          |
      | ESt. Order Date |
      | 5/2022          |
      | total           |
      | quoted          |
      | remaining       |

#
  Scenario: [Opportunity-3] Verify that after selecting an order month, the month pop-up should appear.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    And User tap on "opportunities" button
    And User select opportunity
    And User tap on "month" button
    Then User verifies following option are displayed
      | Field     |
      | January   |
      | February  |
      | March     |
      | April     |
      | May       |
      | June      |
      | July      |
      | August    |
      | September |
      | October   |
      | November  |
      | December  |
#
  Scenario: [Opportunity-4] Verify that the user can delete the opportunity from the info tab.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    And User taps on "+" option
    And User taps on "Add Opportunity" option
    And User fills all required data into their respective field for opportunity
      | Field           |
      | Affiliation     |
      | Customer        |
      | Location        |
      | BOH Role        |
      | Win Probability |
      | Value Breakdown |
    And User taps on "CREATE OPPORTUNITY" option
    And User tap on "opportunities" button
    And User select opportunity
    And User taps on "Delete Opportunity" option
#    Then User verifies message "Removed Opportunity" is displayed
#
  Scenario: [Opportunity-5] Verify that after selecting REs, the user can see the list of REs.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    And User tap on "opportunities" button
    And User select opportunity
    And User tap on "REs" button
    Then User verifies list is displayed
#
  Scenario: [Opportunity-6] Verify that if there are no REs, then it should display the message.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
    And User tap on "opportunities" button
    And User selects "opportunity #16" option
    And User tap on "REs" button
    Then User verifies "No requirement Estimates for opportunity #16" is displayed on page
#Locators are not available for win probability message
#  Scenario Outline: [Opportunity-7] Verify that the user can see the win probability and their respective responses on screen.
#    Given User is on BOH FPU homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Ekal@BOH123!"
#    And User taps on "+" option
#    And User taps on "Add Opportunity" option
#    And User taps on "<Win Probability>" option for validation
#    Then User verifies "<Message>" is displayed on page for validation
#    Examples:
#      |Win Probability|Message                                                       |
#      |      10%      | Providing Information-No Known Requirements                  |
#      |      20%      | Customer Requested Survey-No Known Funding Source            |
#      |      50%      | Customer Wants It-CurrentlySeeking Funding,                  |
#      |      75%      | Customer Wants It-Funding Identified-Awaiting Authorization, |
#      |     100%      | Customer has Provided Document Numbers or Confirmed Purchase |