# Created by m-ele at 8/13/2025
Feature: Change Password

  Background:
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5[contains(text(),'Login to Your Account')]" exists
    When I fill "alena9tester@gmail.com" in element "//input[@name='username']"
    And I fill "Hello" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h3[contains(text(), 'My device ')]" exists
    Then I click on "//a[@class='profile-btn hidden-on-tablet']"

  Scenario: Change password with table
    And Fill out with following table:
      | locator                                                                                    | value       |
      | "//input[@class='el-input__inner' and @id=(//label[contains(.,'Current password')]/@for)]" | Hello       |
      |                                                                                            | NewPassword |
      |                                                                                            | NewPassword |
    Then I click on "//button[contains(.,' Confirm ')]"

