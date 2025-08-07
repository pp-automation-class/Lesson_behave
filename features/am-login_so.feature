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
      | username                        | password        | verification_element                                    |
      | 7nxjno9lr@mozmail.com           | r+WLLX9qwx^:>:3 | //h3[contains(text(), 'My device')]                    |
      | 7nxjno9lrpp@mozmail.com         | r+WLLX9qwx^:>:3 | //p[text()='Sorry, unrecognized username or password.'] |
      | 7nxjno9lrpp@mozmail.com         | xxxxx           | //p[text()='Sorry, unrecognized username or password.'] |
      | 7nxjno9lr@mozmail.com           | xxxxx           | //p[text()='Sorry, unrecognized username or password.'] |
      | Skip                            | xxxxx           | //div[text()='Email is required']                       |
      | 7nxjno9lr@mozmail.com           | Skip            | //div[text()='Password is required']                    |
