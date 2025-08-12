Feature: LinkMyGear Application Login

  Background:
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"

  Scenario: Successful user login with valid credentials
    When I fill "pcs.automationclass@gmail.com" in element "//input[@name='username']"
    And I fill "1234567" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h3[contains(text(), 'My devices')]" exists

  Scenario: Unsuccessful user login with invalid credentials
    When I fill "pcs.automationclass@gmail.com" in element "//input[@name='username']"
    When I fill "xxxxx" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h5" contains text "Account"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists


  Scenario: Login successful with
    And Login with following credentials
      | username                      | password |
      | pcs.automationclass@gmail.com | 1234567  |
    Then I verify element "//h3[contains(text(), 'My devices')]" exists

  Scenario: Login unsuccessful with table
    And Login with following credentials from table
      | field    | value                         |
      | username | pcs.automationclass@gmail.com |
      | password | 1234567                       |
    Then I verify element "//h3[contains(text(), 'My devices')]" exists
