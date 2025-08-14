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
      | username                 | password | verification_element                                    |
      | akr.autotest@gmail.com   | 12345    |  //h3[contains(text(), 'My devices ')]                 |
      | akr.autotest+1@gmail.com | 12345    | //p[text()='Sorry, unrecognized username or password.'] |
      | akr.autotest+2@gmail.com | 13579    | //p[text()='Sorry, unrecognized username or password.'] |
      | autotest@gmail.com       | 13579    | //p[text()='Sorry, unrecognized username or password.'] |
      | Skip                     | 12345    | //div[text()='Email is required']                       |
      | autotest@gmail.com       | Skip     | //div[text()='Password is required']                    |





