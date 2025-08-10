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
      | username                  | password      | verification_element                                    |
      | test12345.sky@gmail.com   | %12345ytkonos | //h3[contains(text(), 'My devices')]                    |
      | test12345.sky+1@gmail.com | %12345ytkonos | //p[text()='Sorry, unrecognized username or password.'] |
      | test12345.sky+2@gmail.com | xxxxx         | //p[text()='Sorry, unrecognized username or password.'] |
      | test12345.sky@gmail.com   | xxxxx         | //p[text()='Sorry, unrecognized username or password.'] |
      | Skip                      | %12345ytkonos | //div[text()='Email is required']                       |
      | test12345.sky@gmail.com   | Skip          | //div[text()='Password is required']                    |
      | Skip                      | Skip          | //div[text()='Email is required']                       |
      | test12345.skygmail.com    | %12345ytkonos | //p[text()='Sorry, unrecognized username or password.'] |
      | test12345.sky@gmailcom    | %12345ytkonos | //p[text()='Sorry, unrecognized username or password.'] |


  Scenario Outline: Forgot password with various credentials
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I click on "//a[text()='Forgot password?']"
    Then I verify element "//h5[contains(text(), 'Restore Password')]" exists
    When I fill "<Your Email>" in element "//input[@class='el-input__inner']"
    And I click on "//button[text()=' Send ']"
    And I verify element "<verification_element>" exists
    When I wait for 1.5 seconds

    Examples:
      | Your Email                | verification_element                                                                                                                 |
      | test12345.sk@+1@gmail.com | //h5[contains(text(),'Please check your inbox')] |
      | test12345.sky+1@gmailcom  | //div[contains(text(),'Please enter a valid email address')]                                                                         |
      | test12345.sky+1gmail.com  | //div[contains(text(),'Please enter a valid email address')]                                                                         |
      | Skip                      | //div[contains(text(),'Please enter you email address')]                                                                             |