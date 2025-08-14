Feature: LinkMyGear Device Settings

    Background:
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I fill "anton.bondarenko.test@gmail.com" in element "//input[@name='username']"
    And I fill "123459" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h3[contains(text(), 'My device ')]" exists

    Scenario: Add new device and delete it
      When I navigate to "https://dev.linkmygear.com/#/device-settings"
      And I click on "//button[.//span[text()='Add new device']]"
      Then  I wait for element "//h3[@class='modal-title' and text()='Add device']" to be visible
      And   I click on "//label[text()='Device type']"
      And   I click on "//li[.//span[text()='Airguard other']]"
      When  I fill "New Test Device" in element "//input[@class='el-input__inner']"
      Then  I click on "//div[@class='form-submit']/button[.//span[text()='Add new device']]"
      And  I click on "//span[normalize-space(.)='New Test Device']/following::button[contains(@class, 'lmg-btn--red') and normalize-space(.)='Delete']"
      Then  I wait for element "//h3[@class='modal-title' and text()='Delete device']" to be visible
      And I click on "//*[contains(@class, 'modal-content-remove-device')]//button[contains(@class, 'lmg-btn--red') and normalize-space(.)='Delete']"
      Then I verify element "//*[contains(@class, 'el-message__content') and contains(normalize-space(.), 'Device deleted')]" exists

