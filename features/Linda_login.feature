Feature: LinkMyGear Application Login
  
  Scenario: Unsuccessful user login with valid name and empty password
    Given I navigate to "https://dev.linkmygear.com/#/login"
    And I verify element "h5" contains text "Account"
    When I fill "alena9tester@gmail.com" in element "//input[@type='text']"
    And I click on "button[@class='lmg-btn lmg-btn--sm']"

    
    Scenario: User forgot password
      Given I navigate to "https://dev.linkmygear.com/#/login"
      And I verify element "h5" contains text "Account"
      When I click on "//div[@class='col-12 text-center mt-3']"
      And I wait for element "//h5[@class='card-title text-center pb-0 fs-4']" to be visible
      When I fill "alena9tester@gmail.com" in element "//input[@class='el-input__inner']"
