Feature: OrangeHRM Registration page
  Scenario: verify the login functionality
    Given I launch OrangeHRM website
    When I enter Admin and admin123 as a user and click login
    Then I verify if the user is successfully login or not


  Scenario Outline: verify the login functionality by giving multiple inputes
    Given I launch OrangeHRM website
    When I enter <username> and <password> as a user and click login
    Then I verify if the user is successfully login or not
    Examples:
    |username|password|
    |admin   |1234    |


  Scenario: Add employee
    Given I launch OrangeHRM website
    When I enter Admin and admin123 as a user and click login
    Then I verify if the user is successfully login or not
    Then I click on PIM and add Employee
    Then I enter firstname Rohit Middlename Kumar Lastname Singh anc click save