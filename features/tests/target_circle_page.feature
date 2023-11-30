# Created by anastasiiatetiura at 11/13/23
Feature:  Target circle page

  Scenario: Verify there are 5 benefit boxes on the page
    Given Open target main page
    When Click Target Circle
    Then Verify there are 5 boxes

  Scenario: user can click through Circle Tabs
    Given Open Circle page
    Then Verify that clicking through tabs works
