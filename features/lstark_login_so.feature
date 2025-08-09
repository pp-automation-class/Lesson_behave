# Created by laurastark at 8/9/25

Feature: LinkMyGear Application Login

# This is a background step that runs before each scenario
  Background:
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"

  Scenario Outline: Login attempts with various credential combinations
    When I fill "<username>" in element "//input[@name='username']"
    When I fill "<password>" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
   # Then I verify element "//h5" contains text "Account"
    Then I verify element "<verification_element>" exists

    Examples:
      | username                   | password   | verification_element                                    |
      | lauravstesting53@gmail.com | T8st8ng38! | //h3[contains(text(),'My device ')]                     |
      | lauravstesting@gmail.com   | xxxxx      | //p[text()='Sorry, unrecognized username or password.'] |
      | lauravstesting53@gmail.com | xxxxx      | //p[text()='Sorry, unrecognized username or password.'] |
      | lauravstesting@gmail.com   | T8st8ng38! | //p[text()='Sorry, unrecognized username or password.'] |
      | lauravstesting53@gmail.com | skip       | //p[text()='Sorry, unrecognized username or password.'] |
      | skip                       | xxxxx      | //p[text()='Sorry, unrecognized username or password.'] |

    # Unable to implement scenario outline for leading/trailing spaces, so created separate scenarios below
    # because the framework trims spaces from variables automatically
    # It is only work if I put spaces between " and <variable> in the When code lines.

  Scenario: Unsuccessful user login with valid email with space at the end and valid password
    When I fill "lauravstesting53@gmail.com " in element "//input[@name='username']"
    And I fill "T8st8ng38!" in element "//input[@name='password']"
    And I click on "//button[@type='submit']"
    Then I verify element "//h5" contains text "Login to Your Account"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

  Scenario: Unsuccessful user login with valid email with leading trailing space and valid password
    When I fill " lauravstesting53@gmail.com" in element "//input[@name='username']"
    And I fill "T8st8ng38!" in element "//input[@name='password']"
    And I click on "//button[@type='submit']"
    Then I verify element "//h5" contains text "Login to Your Account"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

  Scenario: Unsuccessful user login with valid email and valid password with trailing space
    When I fill "lauravstesting53@gmail.com" in element "//input[@name='username']"
    And I fill "T8st8ng38! " in element "//input[@name='password']"
    And I click on "//button[@type='submit']"
    Then I verify element "//h5" contains text "Login to Your Account"
    And I verify element "//p[text()='Sorry, unrecognized username or password.']" exists

  Scenario: Unsuccessful user login with valid email and valid password with leading space
    When I fill "lauravstesting53@gmail.com" in element "//input[@name='username']"
    And I fill " T8st8ng38!" in element "//input[@name='password']"
    And I click on "//button[@type='submit']"
    Then I verify element "//h5" contains text "Login to Your Account"



