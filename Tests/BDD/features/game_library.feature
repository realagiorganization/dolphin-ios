Feature: Manage the game library
  As a player
  I want to add, refresh, and organize my game library
  So that I can find and launch games quickly

  Scenario: Add a new games folder
    Given the user is on the Library screen
    When the user adds a folder with supported game files
    Then the library shows the newly discovered games

  Scenario: Refresh the library after adding games
    Given the user has an existing games folder
    When the user triggers a library refresh
    Then the library updates with any new games

  Scenario: Remove a games folder
    Given the library contains games from a folder
    When the user removes the folder from library sources
    Then the games from that folder are no longer listed
