Feature: LinkMyGear Devices Settings

  Background:
    Given I navigate to "https://dev.linkmygear.com"
    And   I verify element "//h5" contains text "Account"
    When  I fill "7nxjno9lr@mozmail.com" in element "//input[@name='username']"
    And   I fill "r+WLLX9qwx^:>:3" in element "//input[@name='password']"
    And   I click on "//button[text()=' Login ']"
    Then  I verify element "//h3[contains(text(), 'My device')]" exists
    When  I click on "//a[@href='#/device-settings']"
    Then  I verify element "//div[@class='row']/h3[contains(text(), 'Devices Settings')]" exists

  Scenario: Device Settings - Add New Device
    When  I click on "//button[.//span[text()='Add new device']]"
    Then  I wait for element "//h3[@class='modal-title' and text()='Add device']" to be visible
    And   I click on "//label[text()='Device type']"
    And   I click on "//li[.//span[text()='Airguard other']]"
    When  I fill "Test Device #1" in element "//input[@class='el-input__inner']"
    Then  I click on "//div[@class='form-submit']/button[.//span[text()='Add new device']]"
    And   I wait for 2 seconds
