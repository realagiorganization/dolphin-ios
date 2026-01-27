Feature: Tune settings for stability and performance
  As a player
  I want to adjust settings to balance performance and quality
  So that the app runs smoothly on my device

  Scenario: Update graphics backend
    Given the user is on the Graphics settings screen
    When the user selects a different backend
    Then the app saves the selection and applies it on next launch

  Scenario: Enable performance overlays
    Given a game is running
    When the user enables performance overlays
    Then the overlays appear with current metrics

  Scenario: Restore default settings
    Given the user has customized settings
    When the user restores defaults
    Then all settings revert to the recommended values
