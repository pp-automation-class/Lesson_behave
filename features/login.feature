Feature: LinkMyGear Application Login

  Scenario: Successful user login with valid credentials
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I fill "pcs.automationclass@gmail.com" in element "//input[@name='username']"
    When I fill "1234567" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h3[contains(text(), 'My devices ')]" exists
    