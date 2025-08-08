Feature: LinkMyGear Application Login

  Scenario: Successful user login with valid credentials
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I fill "amitha04@gmail.com" in element "//input[@name='username']"
    And I fill "Mypassword" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h3[contains(text(), 'My devices ')]" exists

  Scenario: Unsuccessful user login with invalid credentials
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I fill "amitha05@gmail.com" in element "//input[@name='username']"
    When I fill "Mypassword" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    And I verify element "//p[@class = 'el-message__content']" exists

  Scenario: Unsuccessful user login with Empty email
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I fill "Mypassword" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    And I verify element "//div[text() = 'Email is required']" exists

  Scenario: Unsuccessful user login with Empty password
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I fill "amitha04@gmail.com" in element "//input[@name='username']"
    And I click on "//button[text()=' Login ']"
    And I verify element "//div[text() = 'Password is required']" exists

  Scenario: User able to click on Forgot password link
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I click on "//a[text() = 'Forgot password?']"
    Then I verify element "//h5[text() = 'Restore Password']" exists

  Scenario: User able to click on Forgot password and fill the email
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I click on "//a[text() = 'Forgot password?']"
    And I verify element "//h5" contains text "Restore Password"
    And I fill "amitha04@gmail.com" in element "//input[@id='el-id-5312-331']"
    
    Scenario: User able to create a profile with proper username and password
      Given I navigate to "https://dev.linkmygear.com"
      And I verify element "//h5" contains text "Account"
      When I click on "//a[text() = 'Create an account']"
      Then I verify element "//h5" contains text "Create an Account"
      And I fill "amitha.test@gmail.com" in element "//input[@id='el-id-5312-334']"
      And I click on "//span[@class = 'el-checkbox__inner']"
  