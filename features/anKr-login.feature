# Created by ankrylova at 08/07/25
Feature: LinkMyGear Application Login

  Scenario: Successful user login with valid credentials
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I fill "akr.autotest@gmail.com" in element "//input[@name='username']"
    And I fill "12345" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h3[contains(text(), 'My device ')]" exists

  Scenario: Unsuccessful user login with invalid credentials
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I fill "autotest@gmail.com" in element "//input[@name='username']"
    When I fill "13579" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h5" contains text "Account"
   And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists


