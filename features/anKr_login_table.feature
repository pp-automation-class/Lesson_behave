# Created by ankrylova at 08/07/25
Feature: LinkMyGear Application Login

  Background:
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"

  Scenario: Login successful with
    And Login with following credentials
      | username               | password |
      | akr.autotest@gmail.com | 12345    |
    Then I verify element "//h3[contains(text(), 'My devices')]" exists

  Scenario: Login unsuccessful with table
    And Login with following credentials from table
      | field    | value                  |
      | username | akr.autotest@gmail.com |
      | password | 1234567                |
    Then I verify element "//p[text()='Sorry, unrecognized username or password.']" exists