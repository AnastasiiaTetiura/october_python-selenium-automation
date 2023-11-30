# Created by anastasiiatetiura at 11/5/23
Feature: Search tests
  Scenario: User can search for product
    Given Open target main page
    When Search for coffee
    Then Verify search worked for coffee
    Then Verify coffee in search results url

  Scenario: User can search for product
    Given Open target main page
    When Search for paper towel
    Then Verify search worked for  paper towel
    Then Verify  paper+towel in search results url


  #Scenario Outline:
    #Given Open target main page
    #When Search for <product>
    #Then Verify search worked for <expected_product>
    #Then Verify <expected_url> in search results url
    #Examples:
    #|product       |expected_product   |expected_url   |
    #|lipstick      |lipstick           |lipstick       |
    #|car seat      |car seat           |car+seat       |
    #|detergent     |detergent          |detergent      |





