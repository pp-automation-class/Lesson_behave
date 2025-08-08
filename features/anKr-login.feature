# Created by ankrylova at 08/07/25
Feature: LinkMyGear Application Login

  Scenario: Successful user login with valid credentials
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I fill "akr.autotest@gmail.com" in element "//input[@name='username']"
    And I fill "12345" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h3[contains(text(), 'My device ')]" exists

  Scenario: Unsuccessful user login with invalid credentials
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I fill "autotest@gmail.com" in element "//input[@name='username']"
    When I fill "13579" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h5" contains text " Account"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

  Scenario: Unsuccessful user login with valid email and invalid password
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I fill "akr.autotest@gmail.com" in element "//input[@name='username']"
    When I fill "13579" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

  Scenario: Unsuccessful user login with invalid email and valid password
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I fill "autotest@gmail.com" in element "//input[@name='username']"
    When I fill "12345" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

  Scenario: Unsuccessful user login with empty email field and valid password
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I fill "    " in element "//input[@name='username']"
    When I fill "12345" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

  Scenario: Unsuccessful user login with valid email and empty password field
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I fill "akr.autotest@gmail.com" in element "//input[@name='username']"
    When I fill "   " in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

  Scenario: Unsuccessful user login with valid email and valid password with trailing space
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I fill "akr.autotest@gmail.com" in element "//input[@name='username']"
    When I fill "12345 " in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists
  
  Scenario: Successful user create account with valid credential
    Given I navigate to "https://dev.linkmygear.com"
    Then I click on "//a[text()='Create an account']"
    And I verify element "//h5" contains text "Account"
    When I fill "sekex12269@discrip.com" in element "//div[@class='el-input']//input"
    And I click on "//span[@class='el-checkbox__inner']"
    And I click on "//button[text()=' Register ']"
    #Open Login To Your Account page
    And I verify element "//h5" contains text "Account"