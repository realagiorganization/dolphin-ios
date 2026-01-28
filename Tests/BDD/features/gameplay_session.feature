Feature: Run a gameplay session
  As a player
  I want to launch games and manage my sessions
  So that I can play without losing progress

  Scenario: Launch a game from the library
    Given the library contains a valid game
    When the user selects the game and presses Play
    Then the game launches with the last used settings

  Scenario: Create a save state during gameplay
    Given a game is running
    When the user creates a save state
    Then the save state is stored and listed in Save States

  Scenario: Resume from a save state
    Given a game has at least one save state
    When the user loads the most recent save state
    Then the game resumes from that point
