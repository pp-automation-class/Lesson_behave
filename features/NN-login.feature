# Created by Owner at 8/6/2025
Feature: LinkMyGear Application Login

  Background:
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"

  Scenario: Successful user login with valid credentials
#    Given I navigate to "https://dev.linkmygear.com"
#    And I verify element "//h5" contains text "Account"
    When I fill "pcs.automationclass@gmail.com" in element "//input[@name='username']"
    And I fill "1234567" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h3[contains(text(), 'My devices ')]" exists

  Scenario: Login with non-existing email and valid password
#    Given I navigate to "https://dev.linkmygear.com"
#    And I verify element "//h5" contains text "Account"
    When I enter "invalid@example.com" and the password of an existing user
    Then I should see an invalid credentials error

  Scenario: Login with blank email and password
    When I leave both email and password fields blank
    And I click the login button
    Then I should see required field validation messages

  Scenario: Re-register with the same email after deleting account
    Given I delete the user account for "reuse@example.com"
    When I create a new account with the same email
    Then the registration should succeed

  Scenario: Copy and paste password into password field
    When I paste the valid password into the password field
    Then the login should proceed successfully

  Scenario: Login when subscription has expired
    Given the user's subscription has expired
    When they log in with valid credentials
    Then they should be redirected to a subscription renewal page

    Examples:
    | username                  |   password                     |  ver element
    | pcs.automationclass@gmail.com |  123456                    |  //h3[contains(text(), 'My devices ')]
    | pcs.automationclass@gmail.com |  XXXXXX    |