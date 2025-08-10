Feature: LinkMyGear Application Login

  Background:
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"

  Scenario: Successful user login with valid credentials
    When I fill "test12345.sky@gmail.com" in element "//input[@name='username']"
    And I fill "%12345ytkonos" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h3[contains(text(), 'My devices')]" exists

  Scenario: Unsuccessful user login with invalid username
    When I fill "xxx" in element "//input[@name='username']"
    When I fill "%12345ytkonos" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h5" contains text "Account"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

  Scenario: Unsuccessful user login with empty username
    When I fill "%12345ytkonos" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h5" contains text "Account"
    And I verify element "//div[text()='Email is required']" exists

  Scenario: Unsuccessful user login with empty password
    When I fill "test12345.sky@gmail.com" in element "//input[@name='username']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h5" contains text "Account"
    And I verify element "//div[text()='Password is required']" exists

  Scenario: Forgot password
    When I click on "//a[text()='Forgot password?']"
    Then I verify element "//h5[contains(text(), 'Restore Password')]" exists