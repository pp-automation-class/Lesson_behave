Feature: LinkMyGear Application Login

  Scenario: Successful user login with valid credentials
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I fill "artur.gaidar.test.portnov@gmail.com" in element "//input[@name='username']"
    And I fill "q]w[eprotiyu" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h3[contains(text(), 'My devices ')]" exists

  Scenario: Unsuccessful user login with valid username and invalid password
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I fill "artur.gaidar.test.portnov@gmail.com" in element "//input[@name='username']"
    When I fill "0987654321" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h5" contains text "Account"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

  Scenario: Unsuccessful user login with empty username and empty password
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h5" contains text "Account"
    And I verify element "//div[@class='invalid-feedback'][text()='Password is required']" exists
    And I verify element "//div[@class='invalid-feedback'][text()='Email is required']" exists