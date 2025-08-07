Feature: LinkMyGear Application Login

  Background:
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"

  Scenario: Successful user login with valid credentials
    When I fill "7nxjno9lr@mozmail.com" in element "//input[@name='username']"
    And I fill "r+WLLX9qwx^:>:3" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//span[contains(text(), 'Log out')]" exists

  Scenario: Unsuccessful user login with valid name and invalid password
    When I fill "7nxjno9lr@mozmail.com" in element "//input[@name='username']"
    When I fill "xxxxx" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h5" contains text "Account"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

  Scenario: Unsuccessful user login with valid name and empty password
    When I fill "7nxjno9lr@mozmail.com" in element "//input[@name='username']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h5" contains text "Account"
    And I verify element "//div[@class='invalid-feedback'][text()='Password is required']" exists

 Scenario: Unsuccessful user login with empty name
    When I fill "xxxxx" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h5" contains text "Account"
    And I verify element "//div[@class='invalid-feedback'][text()='Email is required']" exists

  Scenario: User forgot password (uncompleted)
    And I click on "//a[@href='#/restorePassword']"
    Then I wait for element "//h5[text()='Restore Password']" to be visible
    When I fill "7nxjno9lr@mozmail.com" in element "//input[@class='el-input__inner']"
    And I click on "//button[text()=' Send ']"
    #And I verify element "//h5[not(text()='Restore Password')]" exists


