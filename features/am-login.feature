Feature: LinkMyGear Application Login

  Background:
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"

  Scenario: Login successful with
    And Login with following credentials
      | username              | password        |
      | 7nxjno9lr@mozmail.com | r+WLLX9qwx^:>:3 |
    Then I verify element "//h3[contains(text(), 'My device')]" exists

  Scenario: Login successful with table
    And Login with following credentials from table
      | field    | value                 |
      | username | 7nxjno9lr@mozmail.com |
      | password | r+WLLX9qwx^:>:3       |
    Then I verify element "//h3[contains(text(), 'My device')]" exists

  Scenario: Login as user
    When I login special as "user"

  Scenario: Login as admin
    When I login special as "admin"

  Scenario: Login as guest
    When I login special as "guest"

  Scenario: Login as unknown
    When I login special as "Vasya"