Feature: LinkMyGear Application Login

  Scenario: Successful user login with valid credentials
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I fill "7nxjno9lr@mozmail.com" in element "//input[@name='username']"
    And I fill "r+WLLX9qwx^:>:3" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//span[contains(text(), 'Log out')]" exists

  Scenario: Unsuccessful user login with valid name and invalid password
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I fill "7nxjno9lr@mozmail.com" in element "//input[@name='username']"
    When I fill "xxxxx" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h5" contains text "Account"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

  Scenario: Unsuccessful user login with valid name and empty password
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I fill "7nxjno9lr@mozmail.com" in element "//input[@name='username']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h5" contains text "Account"
    And I verify element "//div[@class='invalid-feedback'][text()='Password is required']" exists

 Scenario: Unsuccessful user login with empty name
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I fill "xxxxx" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h5" contains text "Account"
    And I verify element "//div[@class='invalid-feedback'][text()='Email is required']" exists
