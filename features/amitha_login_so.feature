Feature: LinkMyGear Application Login

  Background:
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I fill "amitha04@gmail.com" in element "//input[@name='username']"
    When I fill "Mypassword" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"

  Scenario Outline: Login with various credentials



    Examples:
      | username                        | password | verification_element                                    |
      | pcs.automationclass@gmail.com   | 1234567  | //h3[contains(text(), 'My devices')]                    |
      | pcs.automationclass+1@gmail.com | 1234567  | //p[text()='Sorry, unrecognized username or password.'] |
      | pcs.automationclass+2@gmail.com | xxxxx    | //p[text()='Sorry, unrecognized username or password.'] |
      | pcs.automationclass@gmail.com   | xxxxx    | //p[text()='Sorry, unrecognized username or password.'] |
      | Skip                            | xxxxx    | //div[text()='Email is required']                       |
      | pcs.automationclass@gmail.com   | Skip     | //div[text()='Password is required']                    |
