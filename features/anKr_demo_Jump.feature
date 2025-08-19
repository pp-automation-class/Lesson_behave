# Created by akryl at 8/18/2025
Feature: dev.linkmygear.com DemoJamp

  Background:
    Given I navigate to "dev" environment
    And I verify element "//h5[normalize-space()='Account']" exists
    When I fill "akr.autotest@gmail.com" in element "//input[@name='username']"
    And I fill "12345" in element "//input[@name='password']"
    And I click on "//button[normalize-space()='Login']"
    Then I verify element "//h3[contains(normalize-space(), 'My device')]" exists
    When I click on "//button[contains(.,'Demo Jump')]"
    Then I verify element "//h3[@class='modal-title' and normalize-space()='Generate demo jump']" exists

  Scenario: Open demo jump
    When I click on "//button[contains(.,'Demo Jump')]"
    Then I verify element "//h3[@class='modal-title' and normalize-space()='Generate demo jump']" exists