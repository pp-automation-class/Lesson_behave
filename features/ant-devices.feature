Feature: LinkMyGear Device Settings

    Background:
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When ANT I login as "tester"
    Then I verify element "//h3[contains(text(), 'My devices')]" exists

  Scenario: Add new device and delete it
      When I navigate to "https://dev.linkmygear.com/#/device-settings"
      And ANT I add new device "New test Device"
      Then ANT I delete "New test Device"