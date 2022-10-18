Feature: Fashiondays register feature

    Background:
      Given home: I am a user on fashiondays.ro Home page

    @register
    Scenario: Click contul meu
      When home: I click on contul meu
      When login: click on Fa-ti Cont
      When register: I set my email "htconemus@gmail.com"
      When register: I set my password "Test123!"
      When register: I click on Am citit termeni si conditii
      When register: I click ma abonez
      When register: I click on creaza cont
      Then register: verify error message for wrong email
      Then register: verify error message accept terms and condition
      Then register: verify error message no password



    @register1
    Scenario Outline: Click contul meu variante multiple
      When home: I click on contul meu
      When login: click on Fa-ti Cont
      When register: I set my email "<email>"
      When register: I set my password "<password>"
      When register: I click on Am citit termeni si conditii
      When register: I click ma abonez
      When register: I click on creaza cont
      Then register: verify error message for wrong email
      Then register: verify error messageaccpt terms and condition
      Then register: verify error message no password


    Examples:
      | email                   | password    |
      |mariuscomaneahoo.com     |Test123!|
      |mriuscomaneciu@yahoo.com |      |
      |                         |Test113!|
      |anaaremere1982@gmail.com |Test123!|