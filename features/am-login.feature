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

  Scenario Outline: User registration
    When I click on "//a[@href='#/register']"
    Then I wait for element "//h5[text()='Create an Account']" to be visible
    When I fill "<email>" in element "//input[@class='el-input__inner']"
    And  I click on "//span[@class='el-checkbox__inner']"
    And  I click on "//button[text()=' Register ']"
    When I verify element "<verification_element>" exists
    Then I wait for 2 seconds

    Examples:
      | email                      | verification_element                             |
      | dx5e7nxjno9lr@mozmail.com  | //h3[contains(text(), 'My device')]              |
      | 7nxjno9lr@mozmail.com      | //p[contains(text(), 'The user already exists')] |

  Scenario: User registration with empty email
    When I click on "//a[@href='#/register']"
    Then I wait for element "//h5[text()='Create an Account']" to be visible
    When I click on "//input[@class='el-input__inner']"
    And  I click on "//span[@class='el-checkbox__inner']"
    When I verify element "//div[text()='Please enter you email address']" exists
    Then I wait for 2 seconds

   Scenario: User registration with invalid email
    When I click on "//a[@href='#/register']"
    Then I wait for element "//h5[text()='Create an Account']" to be visible
    When I fill "xxxxx" in element "//input[@class='el-input__inner']"
    And  I verify element "//div[text()='Please enter a valid email address']" exists
    Then I wait for 2 seconds

