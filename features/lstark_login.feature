# Created by laurastark at 8/6/25
Feature: LinkMyGear Application Login

  Scenario: Successful user login with valid credentials
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I fill "lauravstesting53@gmail.com" in element "//input[@name='username']"
    And I fill "T8st8ng38!" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h3[contains(text(), 'My devices ')]" exists

  Scenario: Unsuccessful user login with both invalid credentials
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I fill "pcs.automationclass@gmail.com" in element "//input[@name='username']"
    When I fill "xxxxx" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h5" contains text "Account"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

  Scenario: Unsuccessful user login with valid email and invalid password
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Login to Your Account"
    When I fill "lauravstesting53@gmail.com" in element "//input[@name='username']"
    And I fill "T8st8ng38" in element "//input[@name='password']"
    And I click on "//button[@type='submit']"
    Then I verify element "//h5" contains text "Login to Your Account"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

  Scenario: Unsuccessful user login with invalid email and valid password
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Login to Your Account"
    When I fill "lauravstesting5@gmail.com" in element "//input[@name='username']"
    And I fill "T8st8ng38" in element "//input[@name='password']"
    And I click on "//button[@type='submit']"
    Then I verify element "//h5" contains text "Login to Your Account"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

  Scenario: Unsuccessful user login with valid email and empty password field
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Login to Your Account"
    When I fill "lauravstesting5@gmail.com" in element "//input[@name='username']"
    And I click on "//button[@type='submit']"
    Then I verify element "//h5" contains text "Login to Your Account"
    And I verify element "//div[text()='Password is required']" exists

  Scenario: Unsuccessful user login with empty email field and valid password
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Login to Your Account"
    When I fill "T8st8ng38" in element "//input[@name='password']"
    And I click on "//button[@type='submit']"
    Then I verify element "//h5" contains text "Login to Your Account"
    And I verify element "//div[text()='Email is required']" exists

  Scenario: Unsuccessful user login with valid email with space at the end and valid password
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Login to Your Account"
    When I fill "lauravstesting53@gmail.com " in element "//input[@name='username']"
    And I fill "T8st8ng38!" in element "//input[@name='password']"
    And I click on "//button[@type='submit']"
    Then I verify element "//h5" contains text "Login to Your Account"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

Scenario: Unsuccessful user login with valid email with leading trailing space and valid password
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Login to Your Account"
    When I fill " lauravstesting53@gmail.com" in element "//input[@name='username']"
    And I fill "T8st8ng38!" in element "//input[@name='password']"
    And I click on "//button[@type='submit']"
    Then I verify element "//h5" contains text "Login to Your Account"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

  Scenario: Unsuccessful user login with valid email and valid password with trailing space
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Login to Your Account"
    When I fill "lauravstesting53@gmail.com" in element "//input[@name='username']"
    And I fill "T8st8ng38! " in element "//input[@name='password']"
    And I click on "//button[@type='submit']"
    Then I verify element "//h5" contains text "Login to Your Account"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

    Scenario: Unsuccessful user login with valid email and valid password with leading space
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Login to Your Account"
    When I fill "lauravstesting53@gmail.com" in element "//input[@name='username']"
    And I fill " T8st8ng38!" in element "//input[@name='password']"
    And I click on "//button[@type='submit']"
    Then I verify element "//h5" contains text "Login to Your Account"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists