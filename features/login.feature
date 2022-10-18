Feature: Fashiondays login feature

    Background:
      Given home: I am a user on fashiondays.ro Home page

    @login3
    Scenario: Click customer logo
      When home: I click on contul meu
      When login: I set my email "mariuscomaneciu@yahoo.com"
      When login: I set my password "gk960474" and click Continua
      Then login: Verify if error message is received

    @login
    Scenario Outline: Click logo button and return to home
      When home: I click on contul meu
      When login: I set my email "<email>"
      When login: I set my password "<password>" and click Continua
      Then login: Verify if error message is received


    Examples:
      | email                   | password    |
      |mariuscomaneciu@yahoo.com|gk960474|
      |mriuscomaneciu@yahoo.com|gk960474|
      |mariuscomaneciu@yahoo.com|gak960474|
      |anaaremere1982@gmail.com|Test123!|







