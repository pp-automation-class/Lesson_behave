# Created by ankrylova at 08/07/25
Feature: LinkMyGear Application Login

  Background:
#    Given anKr I navigate to "https://dev.linkmygear.com"
    Given anKr I navigate to "dev" environment
#    And anKr I verify element "//h5" contains text "Account"
    And anKr I verify element page title contains text "Account"


  Scenario: Successful user login with valid credentials
    When anKr I login as "user"
    Then anKr I verify element "//h3[contains(text(),'My device')]" exists

  Scenario: Unsuccessful user login with invalid credentials
    When I fill "autotest@gmail.com" in element "//input[@name='username']"
    When I fill "13579" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h5" contains text " Account"
    Then I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

  Scenario: Unsuccessful user login with valid email and invalid password
    When I fill "akr.autotest@gmail.com" in element "//input[@name='username']"
    When I fill "13579" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

  Scenario: Unsuccessful user login with invalid email and valid password
    When I fill "autotest@gmail.com" in element "//input[@name='username']"
    When I fill "12345" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

  Scenario: Unsuccessful user login with empty email field and valid password
    When I fill "    " in element "//input[@name='username']"
    When I fill "12345" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

  Scenario: Unsuccessful user login with valid email and empty password field
    When I fill "akr.autotest@gmail.com" in element "//input[@name='username']"
    When I fill "   " in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

  Scenario: Unsuccessful user login with valid email and valid password with trailing space
    When I fill "akr.autotest@gmail.com" in element "//input[@name='username']"
    When I fill "12345  " in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//p[text()='Sorry, unrecognized username or password.']" exists


