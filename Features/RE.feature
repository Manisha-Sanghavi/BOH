# Created by rashm at 21/04/2022
Feature: RE

  Scenario : Verify User can sort REs with different drop down options list
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on RE tab
    And User taps on "Sort By" option
    And User select <sort by> option
    Then "REs" list is sorted and displayed
      | sort by |
      | Recent Activity |
      | RE Date |
      | Value |
      | REID |
      | Location |
      | CSM |
      | Status |

    Scenario : Verify User can sort REs in descending order of REID
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on RE tab
    And User taps on "Sort By" option
    And User select <sort by> option
    Then User Verifies REs diplayed are in descending order of REID

  Scenario Outline: Verify User can filter REs by different filter options [Current, All, Draft, Validate, Inactive, Active, Pending, Awarded, Complete]
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User can see "Customer Management" page
    And User taps on RE tab
    And User taps on "Filter By" option
    And User select <filter by> option
    Then "REs" list is displayed
    Examples:
      | filter by |
      |Current|
      | All |
      |Draft|
      |Validate|
      |Inactive|
      |Active|
      |Pending|
      |Awarded|
      |Complete|

