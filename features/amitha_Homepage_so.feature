Feature: LinkMyGear Application Login

  Background:
    Given I navigate to "https://dev.linkmygear.com"
    And I verify element "//h5" contains text "Account"
    When I fill "amitha04@gmail.com" in element "//input[@name='username']"
    When I fill "Mypassword" in element "//input[@name='password']"
    And I click on "//button[text()=' Login ']"

  Scenario Outline: Verify if the Blog items are present
   // And I verify element "<XPATH>" contains text "<TEXT>"
   // And I verify element "<XPATH>" exists
    When I click on "<XPATH>"
    And I verify element "<Blog Title>" exists



    Examples:
      | XPATH                                                                                                                  | Blog Title                                                                  |
      | //h4[contains(text(),'Parachute Advansed Jasmine Supports Jyothi Yarraji')]/following::button[text() = 'Read more'][1] | //h4[contains(text(),'Parachute Advansed Jasmine Supports Jyothi Yarraji')] |
      | //h4[contains(text(),'Switzerland is an ideal host for the athletes from')]/following::button[text() = 'Read more'][1] | //h4[contains(text(),'Switzerland is an ideal host for the athletes from')] |
      | //h4[contains(text(),'Military World Winter Games 2025')]/following::button[text() = 'Read more'][1]                   | //h4[contains(text(),'Military World Winter Games 2025')]                   |
      | //h4[contains(text(),'Parachute Regiment beaten by Royal Guard in charit')]/following::button[text() = 'Read more'][1] | //h4[contains(text(),'Parachute Regiment beaten by Royal Guard in charit')] |
      | //h4[contains(text(),'In collaboration with Skydive Pharaohs, the first')]/following::button[text() = 'Read more'][1]  | //h4[contains(text(),'In collaboration with Skydive Pharaohs, the first')]  |