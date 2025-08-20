# Created by Kate at 8/14/2025
Feature: LinkMyGear Add New Device

  Background:
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I fill "katedtest@gmail.com" in element "//input[@name='username']"
    And I fill "1234567890" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h3[contains(text(), 'My devices')]" exists

  Scenario: Add new device
    When I click on "//a[@class='section-title__icon']"
    Then I verify element "//h3" contains text "Devices Settings"
    When I click on "//span[text()='Add new device']"
    Then I verify element "//h3[text()='Add device']" contains text "Add"
    When I click on "//div[@class='el-select']"
    And I click on "//li/span[text()='Airguard other']"
    And I fill "iPhone 16 Pro" in element "//input[@class='el-input__inner']"
    And I click on "//div[@class='modal-content']//button[.//span[text()='Add new device']]"
    Then I verify element "//span[text()='iPhone 16 Pro']" exists

  Scenario: Delete added device
    When I click on "//a[@class='section-title__icon']"
    Then I verify element "//h3" contains text "Devices Settings"
    And I verify element "//span[text()='iPhone 16 Pro']" exists
    When I click on "//tr[@class='el-table__row' and .//span[text()='iPhone 16 Pro']]//button[text()=' Delete ']"
    Then I verify element "//h3[text()='Delete device']" exists
    When I click on "//button[text()='Delete']"