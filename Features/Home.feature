@ios_Home @ios_all
Feature:Home


  @ios_NAT-1 @ios_Login @smoke
  Scenario:Verification of request information by mail in Club Deal property
#    Given I reset "testuser31"
    Given I am on app home page
    And I Login with user "testuser31"
    And I create security pin for "testuser31"
    When I tap on club deals tab
    And I select 'Request Information-Clubdeal' property from club deals tab
    And I tap on Request information button
    And I tap "Information by mail" button
    Then I see message 'We would be happy to send you further background information on this project.'

     @ios_NAT-2 @ios_clubdeal
  Scenario: Verify text for Club Deal property with Funding phase
#    Given I reset "testuser31"
    Given I am on app home page
    And I Login with user "testuser31"
    And I create security pin for "testuser31"
    When I tap on club deals tab
    And I can see 'Funding Phase-Clubdeal' property on club deals tab
    Then I verify following text details of property 'Nova Living! Rahlstedt' in culb deal tab
    |Phase                  |      Property              |      scope                | Total acquisition price  |	Finanzierungsvolumen |	Predicted Total return p.a. * |FundingPercent       |
    |	Funding closed      |	Nova Living! Rahlstedt    |  18 Neubauwohnungen       |    	8.305.849 €          | 		3.500.000 €   |	       7.85 %                     | 	100 %           |

     @ios_NAT-3 @ios_login
  Scenario Outline: Verify user cannot login with invalid user credentials
    Given I am on Finexity home page
      When I click on login button
      And I enter the username "<username>"
      And I enter the password for "<password>"
      And I click on sign in button
      Then I verify that user see "<message>" alert
      Examples:
        |      username           |   password        |  message                         |
        |   tesur34@finexitycom   |  !finexity2020    |   E-Mail Address invalid         |
        |  tesuser34@finexity.com |   finexity2020    |   Wrong email or password.       |