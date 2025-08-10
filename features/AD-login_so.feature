Feature: LinkMyGear Application Login

  Scenario Outline: Login with various credentials
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I fill "<username>" in element "//input[@name='username']"
    When I fill "<password>" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"
    And I verify element "<verification_element>" exists
    When I wait for 1 seconds


    Examples:
      | username                        | password | verification_element                                   |
      | test12345.sky@gmail.com   | %12345ytkonos | //h3[contains(text(), 'My devices')]                    |
      | test12345.sky+1@gmail.com | %12345ytkonos | //p[text()='Sorry, unrecognized username or password.'] |
      | test12345.sky+2@gmail.com | xxxxx         | //p[text()='Sorry, unrecognized username or password.'] |
      | test12345.sky@gmail.com   | xxxxx         | //p[text()='Sorry, unrecognized username or password.'] |
      | Skip                      | %12345ytkonos | //div[text()='Email is required']                       |
      | test12345.sky@gmail.com   | Skip          | //div[text()='Password is required']                    |
