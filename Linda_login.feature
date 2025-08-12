  Feature: LinkMyGear Application Login

    Background:
      Given I navigate to "https://dev.linkmygear.com"
      And I verify element "//h5[contains(text(),'Login to Your Account')]" exists
      
    Scenario: Successful user login with valid credentials
      When I fill "alena9tester@gmail.com" in element "//input[@name='username']"
      And I fill "Hello" in element "//input[@name='password']"
      And I click on "//button[text()=' Login ']"
      Then I verify element "//h3[contains(text(), 'My device ')]" exists

      Scenario: Unsuccessful user login with invalid credential
        When I fill "alena9tester@gmail.com" in element "//input[@name='username']"
        And I fill "12345" in element "//input[@name='password']"
        Then I verify element "//h5[contains(text(),'Login to Your Account')]" exists


