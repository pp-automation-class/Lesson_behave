Feature: LinkMyGear Application Login

  Scenario Outline: Login with various credentials
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I fill "<username>" in element "//input[@name='username']"
    When I fill "<password>" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    And I verify element "<verification_element>" exists
    When I wait for 2 seconds


    Examples:
      | username                 | password  | verification_element                                    |
      | sergiom.sdet@gmail.com   | Pinklove1 | //h3[contains(text(), 'My devices')]                    |
      | sergiom.sdet@gmail.com   | Pinklove1 | //p[text()='Sorry, unrecognized username or password.'] |
      | sergiom.sdet+2@gmail.com | 123456    | //p[text()='Sorry, unrecognized username or password.'] |
      | sergiom.sdet@gmail.com   | 123456    | //p[text()='Sorry, unrecognized username or password.'] |
      | Skip                     | 456789    | //div[text()='Email is required']                       |
      | sergiom.sdet@gmail.com   | Skip      | //div[text()='Password is required']