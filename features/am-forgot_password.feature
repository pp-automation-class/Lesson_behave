Feature: LinkMyGear Application Login

  Background:
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"

  Scenario: User forgot password
    When I click on "//a[@href='#/restorePassword']"
    Then I wait for element "//h5[text()='Restore Password']" to be visible
    When I fill "7nxjno9lr@mozmail.com" in element "//input[@class='el-input__inner']"
    And  I click on "//button[text()=' Send ']"
    Then I wait for 5 seconds