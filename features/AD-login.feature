Feature: LinkMyGear Application Login

  Background:
    Given User navigates to "https://dev.linkmygear.com"
    And User verify element "//h5" contains text "Account"

  Scenario: Successful user login with valid credentials
    When User fill "test12345.sky@gmail.com" in element "//input[@name='username']"
    And User fill "%12345ytkonos" in element "//input[@name='password']"
    And User click on "//button[text()=' Login ']"
    Then User verify element "//h3[contains(text(),'My device')]" exists

  Scenario: Unsuccessful user login with invalid username
    When User fill "xxx" in element "//input[@name='username']"
    When User fill "%12345ytkonos" in element "//input[@name='password']"
    And User click on "//button[text()=' Login ']"
    Then User verify element "//h5" contains text "Account"
    And User verify element "//p[text()='Sorry, unrecognized username or password.']" exists

  Scenario: Unsuccessful user login with empty username
    When User fill "%12345ytkonos" in element "//input[@name='password']"
    And User click on "//button[text()=' Login ']"
    Then User verify element "//h5" contains text "Account"
    And User verify element "//div[text()='Email is required']" exists

  Scenario: Unsuccessful user login with empty password
    When User fill "test12345.sky@gmail.com" in element "//input[@name='username']"
    And User click on "//button[text()=' Login ']"
    Then User verify element "//h5" contains text "Account"
    And User verify element "//div[text()='Password is required']" exists

  Scenario: Forgot password
    When User click on "//a[text()='Forgot password?']"
    Then User verify element "//h5[contains(text(), 'Restore Password')]" exists
  
  Scenario: Comeback to login from Forgot password
    When User click on "//a[text()='Forgot password?']"
    Then User verify element "//h5[contains(text(), 'Restore Password')]" exists
    And User click on "//a[text()='Back to Login page']"
    Then User verify element "//h5[contains(text(), 'Login to Your Account')]" exists
        
  Scenario: Create an account
    When User click on "//a[text()='Create an account']"
    Then User verify element "//h5[contains(text(), 'Create an Account')]" exists

  Scenario: Comeback to login from Create an account
    When User click on "//a[text()='Create an account']"
    Then User verify element "//h5[contains(text(), 'Create an Account')]" exists
    And User click on "//a[text()='Log in']"
    Then User verify element "//h5[contains(text(), 'Login to Your Account')]" exists

  Scenario: Go to Terms and Conditions
    When User click on "//a[text()='Create an account']"
    Then User verify element "//h5[contains(text(), 'Create an Account')]" exists
    And User click on "//a[text()='Terms and Conditions']"
    Then I navigate to "https://linkmygear.com/terms-and-conditions/"
    And User verify element "//h1[text()='Terms And Conditions']" exists