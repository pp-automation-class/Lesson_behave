# Created by Kate at 8/12/2025
Feature: LinkMyGear Application Login

  Background:
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"

  Scenario: Successful user login with valid credentials
    When I fill "katedtest@gmail.com" in element "//input[@name='username']"
    And I fill "1234567890" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h3[contains(text(), 'My devices')]" exists

  Scenario: Unsuccessful user login with invalid credentials
    When I fill "katedtest@gmail.com" in element "//input[@name='username']"
    When I fill "123456789" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h5" contains text "Account"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

  Scenario: Error message with provided user email but an empty password
    When I fill "katedtest@gmail.com" in element "//input[@name='username']"
    When I click on "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//div[text()='Password is required']" exists

  Scenario: Error message with an empty user email but valid password
    When I fill "123456789" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//div[text()='Email is required']" exists

  Scenario: Error message with an empty email and an empty password
    When I click on "//button[text()=' Login ']"
    Then I verify element "//div[text()='Email is required']" exists
    And I verify element "//div[text()='Password is required']" exists

  Scenario: "Forgot password" link redirects to Restore Password page
    When I click on "//a[text()='Forgot password?']"
    Then I verify element "//h5" contains text "Restore Password"

  Scenario: "Back to Login page" link redirects to Restore Password page
    When I click on "//a[text()='Forgot password?']"
    And I click on "//a[text()='Back to Login page']"
    Then I verify element "//h5" contains text "Account"

  Scenario: "Create an account" link redirects to Create an Account page
    When I click on "//a[text()='Create an account']"
    Then I verify element "//h5" contains text "Create"

