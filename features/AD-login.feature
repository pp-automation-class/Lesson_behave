Feature: LinkMyGear Application Login

  Background:
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"

  Scenario: Successful user login with valid credentials
    When I fill "test12345.sky@gmail.com" in element "//input[@name='username']"
    And I fill "%12345ytkonos" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h3[contains(text(),'My device')]" exists

  Scenario: Unsuccessful user login with invalid username
    When I fill "xxx" in element "//input[@name='username']"
    When I fill "%12345ytkonos" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h5" contains text "Account"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

  Scenario: Unsuccessful user login with empty username
    When I fill "%12345ytkonos" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h5" contains text "Account"
    And I verify element "//div[text()='Email is required']" exists

  Scenario: Unsuccessful user login with empty password
    When I fill "test12345.sky@gmail.com" in element "//input[@name='username']"
    And I click on "//button[text()=' Login ']"
    Then I verify element "//h5" contains text "Account"
    And I verify element "//div[text()='Password is required']" exists

  Scenario: Forgot password
    When I click on "//a[text()='Forgot password?']"
    Then I verify element "//h5[contains(text(), 'Restore Password')]" exists
  
  Scenario: Comeback to login from Forgot password
    When I click on "//a[text()='Forgot password?']"
    Then I verify element "//h5[contains(text(), 'Restore Password')]" exists
    And I click on "//a[text()='Back to Login page']"
    Then I verify element "//h5[contains(text(), 'Login to Your Account')]" exists
        
  Scenario: Create an account
    When I click on "//a[text()='Create an account']"
    Then I verify element "//h5[contains(text(), 'Create an Account')]" exists

  Scenario: Comeback to login from Create an account
    When I click on "//a[text()='Create an account']"
    Then I verify element "//h5[contains(text(), 'Create an Account')]" exists
    And I click on "//a[text()='Log in']"
    Then I verify element "//h5[contains(text(), 'Login to Your Account')]" exists

  Scenario: Go to Terms and Conditions
    When I click on "//a[text()='Create an account']"
    Then I verify element "//h5[contains(text(), 'Create an Account')]" exists
    And I click on "//a[text()='Terms and Conditions']"
    Then I navigate to "https://linkmygear.com/terms-and-conditions/"
    And I verify element "//h1[text()='Terms And Conditions']" exists