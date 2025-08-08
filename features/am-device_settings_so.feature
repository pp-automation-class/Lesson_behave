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

  Scenario: Device Settings - Update Device Name
    Then I wait for 5 seconds
    #When  I click on "//button[@aria-label='Edit device name']"