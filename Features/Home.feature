@ios_Home @ios_all
Feature:Home


  @ios_NAT-1 @ios_Login @smoke
  Scenario:Verify the User can Sign In with valid credentials
#    Given I reset "testuser31"
    Given User is on app home page
    And User taps on Already have an account button
    And User enters username "testphprimary5@spurqlabs.com"
    And User enters password "start@101"
    And User taps on Login button
    Then Homepage is displayed

