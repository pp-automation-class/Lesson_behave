Feature: LinkMyGear Demo Jump

  Background:
    Given I navigate to "https://dev.linkmygear.com"
    And   I verify element "//h5" contains text "Account"
    When  I fill "7nxjno9lr@mozmail.com" in element "//input[@name='username']"
    And   I fill "r+WLLX9qwx^:>:3" in element "//input[@name='password']"
    And   I click on "//button[text()=' Login ']"
    Then  I verify element "//h3[contains(text(), 'My device')]" exists
    When  I click on "//button[contains(.,'Demo Jump')]"
    Then  I verify element "//div/h3[@class='modal-title' and .='Generate demo jump']" exists

  Scenario: Generate demo jump - Cancel
    When  I click on "//button[@class='modal-close']"
    Then  I verify element "//h3[contains(text(), 'My device')]" exists

  Scenario: Generate demo jump - Empty Event date
    When  I click on "//div[@class='form-submit']/button/span[contains(.,'Generate demo jump')]"
    Then  I verify element "//div[@class='el-form-item__error' and contains(.,'Please select date and time')]" exists

  Scenario: Generate demo jump with valid current date and time
    When  I click on "//input[@placeholder='Select date and time']"
    And   I click on "//div[@class='el-picker-panel__footer']/button[.='OK']"
    Then  I click on "//div[@class='form-submit']/button/span[contains(.,'Generate demo jump')]"
    And   I wait for element "//p[@class='el-message__content' and .='Demo jump has been generated']" to be visible

  Scenario: Generate demo jump with valid current date and time and As group jump
    When  I click on "//input[@placeholder='Select date and time']"
    And   I click on "//div[@class='el-picker-panel__footer']/button[.='OK']"
    And   I click on "//label[@class='el-form-item__label' and .='As group jump']"
    Then  I click on "//div[@class='form-submit']/button/span[contains(.,'Generate demo jump')]"
    And   I wait for element "//p[@class='el-message__content' and .='Demo jump has been generated']" to be visible