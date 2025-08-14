Feature: LinkMyGear Application Login

  Scenario Outline: Login with various credentials
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I fill "<username>" in element "//input[@name='username']"
    When I fill "<password>" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    And I verify element "<verification_element>" exists



    Examples:
      | username                    | password | verification_element                                    |
      | testanya108+amn@gmail.com   | 55555    | //h3[contains(text(), 'My devices')]                    |
      | testanya108+amn+1@gmail.com | 55555    | //p[text()='Sorry, unrecognized username or password.'] |
      | testanya108+amn+2@gmail.com | xxxxx    | //p[text()='Sorry, unrecognized username or password.'] |
      | testanya108+amn@gmail.com   | xxxxx    | //p[text()='Sorry, unrecognized username or password.'] |
      | Skip                        | xxxxx    | //div[text()='Email is required']                       |
      | testanya108+amn@gmail.com   | Skip     | //div[text()='Password is required']                    |