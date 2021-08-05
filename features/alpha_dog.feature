Feature: Beer description validation
  As a user, we want to validate the correct beer description in the UI

  Background: appium setup
    Given appium is setup
      

  Scenario: alpha dog beer description validation
      Given the main page is shown
       When the user enters in alpha dog
       Then the description is correct