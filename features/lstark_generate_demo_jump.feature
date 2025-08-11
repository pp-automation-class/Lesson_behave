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
    And I click on "//button[@class='lmg-btn lmg-btn--sm lmg-btn--no-nw lmg-btn--orange hidden-on-tablet']"
    And I verify element "//h3[@class='modal-title']" exists
    And I click on "//input[@placeholder='Select date and time']"
    And I click on "//input[@id='el-id-9725-117']"
    And I click on "//td[@class='available today current']"
    And I click on "//div[contains(@class,'el-date-table-cell') and text()='10']"
    #And I click on "//div[@class='el-input__wrapper is-focus']"
    #And I click on "//li[contains(@class,'el-time-spinner__item is-active') and text()='02']"

  #Xpath for hour //li[contains(@class,'el-time-spinner__item is-active') and text()='02']
   # And I click on "//li[contains(@class,'el-time-spinner__item is-active') and text()='30']"
  # XPath for minutes //li[contains(@class,'el-time-spinner__item is-active') and text()='30']
    #And I click on "//li[contains(@class,'el-time-spinner__item is-active') and text()='00']"
  # XPath for seconds //li[contains(@class,'el-time-spinner__item is-active') and text()='00'
    #And I click on "//button[text()='OK']""