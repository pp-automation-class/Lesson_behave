Feature: LinkMyGear Application Login

  Background:
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"

  Scenario: Successful user login with valid credentials
    When I fill "sergiom.sdet@gmail.com" in element "//input[@name='username']"
    And I fill "Pinklove1" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h3[contains(text(), 'My devices')]" exists

  Scenario: Unsuccessful user login with invalid credentials
    When I fill "sergiom.sdet@gmail.com" in element "//input[@name='username']"
    When I fill "1234567" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

  Scenario: Unsuccessful user login with valid email and invalid password
    When I fill "sergiom.sdet@gmail.com" in element "//input[@name='username']"
    When I fill "Pinklove2" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

  Scenario: Unsuccessful user login with empty email and valid password
    When I fill "   " in element "//input[@name='username']"
    And I fill "Pinklove1" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

  Scenario: Unsuccessful user login with valid email and space after password
    When I fill "sergiom.sdet@gmail.com" in element "//input[@name='username']"
    And I fill "Pinklove1 " in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

  Scenario: Successful user login with valid email and password, then logout
    When I fill "sergiom.sdet@gmail.com" in element "//input[@name='username']"
    And I fill "Pinklove1" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h3[contains(text(), 'My devices')]" exists
    Then I verify element "//button[@class='lmg-btn hidden-on-tablet']" contains text "Log out"
    Then I click on "//button[@class='lmg-btn hidden-on-tablet']//span[text()='Log out']"