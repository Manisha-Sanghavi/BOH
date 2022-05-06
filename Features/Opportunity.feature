Feature: Verify Feature: Verify Functionalities for Opportunity module

  Scenario: [Opportunity-1] Verify that the user can create a new opportunity successfully.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "+" option
    And User taps on "Add Opportunity" option
    And User fills all required data into their respective field for opportnity
        |Affiliation|Customer Location|BOH Role|Customer Contact(New/Existing)|Rank or Title|Contact First Name|Contact Last Name|Contact Email|Contact Phone|Win Probability|Value Breakdown|
    And User taps on "Create Opportunity" option
    And User taps on "Opportunity" option
    Then user verifies "Opportunity #" is displayed on page

  Scenario: [Opportunity-2]Verify that the user can see the opportunities summary part displayed on the page.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Opportunities" option
    Then User verifies folllowing options are displayed
      | Opportunity #60      | Est Order Date |115th BSB SSA 1ABCT |
      |7/2022               |Fort Hood, TX   |                    |
      |$7K                  |$0.00           |$7K                 |
      |Total                |Quoted          |Remaining           |


  Scenario: [Opportunity-3] Verify that after selecting an order month, the month pop-up should appear.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Opportunities" option
    And User selects "opportunity #60" opportunity
    And User taps on "order month" option
    Then User verifies following options are displayed
      | January | February | March     | April   | May      | June     |
      | July    | August   | September | October | November | December |

  Scenario: [Opportunity-4] Verify that the user can delete the opportunity from the info tab.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "+" option
    And User taps on "Add Opportunity" option
    And User fills all required data into their respective field for opportunity
        |Affiliation|Customer Location|BOH Role|Customer Contact(New/Existing)|Rank or Title|Contact First Name|Contact Last Name|Contact Email|Contact Phone|Win Probability|Value Breakdown|
    And User taps on "Create Touchbase" option
    And User click on created opportunity
    And User taps on "INFO" option
    And User taps on "Delete" option
    Then User verifies meassage "Removed Opportunity #" is displayed

  Scenario: [Opportunity-5] Verify that after selecting REs, the user can see the list of REs.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Opportunities" option
    And User selects "opportunity #60" option
    And User taps on "REs" option
    Then User verifies "REs list" is displayed on page

  Scenario: [Opportunity-6] Verify that if there are no REs, then it should display the message.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Opportunities" option
    And User select "opportunity #60" option
    And User taps on "REs" option
    Then User verifies "No requirement Estimates for opportunity #60" is displayed on page

  Scenario Outline: [Opportunity-7] Verify that the user can see the win probability and their respective responses on screen.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "+" option
    And User taps on "Add Opportunity" option
    And User taps on "<Win Probability>" option
    Then User verifies "<Message>" is displayed on page
    Examples:
      |Win Probability|Message                                                       |
      |      10%      | Providing Information-No Known Requirements                  |
      |      20%      | Customer Requested Survey-No Known Funding Source            |
      |      50%      | Customer Wants It-CurrentlySeeking Funding,                  |
      |      75%      | Customer Wants It-Funding Identified-Awaiting Authorization, |
      |     100%      | Customer has Provided Document Numbers or Confirmed Purchase |