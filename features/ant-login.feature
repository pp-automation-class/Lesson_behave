Feature: LinkMyGear Application Login

    Background:
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"

    Scenario: Successful user login with valid credentials
    When ANT I login as "tester"
    Then I verify element "//h3[contains(text(), 'My devices')]" exists

    Scenario: Unsuccessful user login with invalid credentials
    When ANT I login as "admin"
    Then I verify element "//h5" contains text "Account"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists
