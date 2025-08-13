Feature: Fill Out My Profile

  Background:
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5[contains(text(),'Login to Your Account')]" exists
    When I fill "alena9tester@gmail.com" in element "//input[@name='username']"
    And I fill "Hello" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h3[contains(text(), 'My device ')]" exists
    Then I click on "//a[@class='profile-btn hidden-on-tablet']"

  Scenario: Fill out my profile with table
    And Fill out with following table:
      | locator                                                                            | value      |
      | "//input[@class='el-input__inner' and @id=//label[contains(.,'First name')]/@for]" | Alena      |
      | "//input[@class='el-input__inner' and @id=//label[contains(.,'Last name')]/@for]"  | Tester     |
    Then I click on "//button[contains(.,' Confirm ')]"


