# Created by laurastark at 8/10/25
Feature: LinkMyGear Application Generate Demo Jump
  # Enter feature description here
  Background:
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"


  Scenario: Generate Demo Jump
    When I fill "lauravstesting53@gmail.com" in element "//input[@name='username']"
    And I fill "T8st8ng38!" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    And I verify element "//h3[contains(text(), 'My device')]" exists
    And I click on "//button[contains(@class,'lmg-btn lmg-btn--sm lmg-btn--no-nw lmg-btn--orange hidden-on-tablet') and text()=' Demo Jump ']"
    And I verify element "//h3[@class='modal-title']" contains text "Generate demo jump"
    And I click on "//input[@placeholder='Select date and time']"
    And I wait for 2 seconds
    #This is the "OK" button in the date picker
    And I click on "//button[@class='el-button el-button--small is-plain el-picker-panel__link-btn']"
    # or use XPath "//button[normalize-space()='OK']"
    And I click on "//button[normalize-space()='Generate demo jump']"
    Then I verify element "//p[text()='Demo jump has been generated']" exists


