Feature: LinkMyGear Application Login

  Scenario: Successful user login with valid credentials
    When I fill "ToasterPower88@gmail.com" in element "//input[@name='username']"
    And I fill "ToasterPower88!" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h3[contains(text(), 'My devices')]" exists

  Scenario: Unsuccessful user login with invalid credentials
    When I fill "ToasterPower88@gmail.com" in element "//input[@name='username']"
    When I fill "xxxxxxx" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h5" contains text "Account"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

    Scenario: Unsuccessful user login with invalid credentials
    When I fill "ToasterPower88@gmail.com" in element "//input[@name='username']"
    When I fill " " in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h5" contains text "Account"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

      Scenario: Unsuccessful user login with invalid credentials
    When I fill "ToasterPower@gmail.com" in element "//input[@name='username']"
    When I fill "ToasterPower88!" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h5" contains text "Account"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists