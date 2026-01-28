Feature: Configure controllers
  As a player
  I want to map inputs and select controller profiles
  So that gameplay feels consistent across devices

  Scenario: Map a Bluetooth controller
    Given a Bluetooth controller is connected
    When the user opens the controller mapping screen
    Then the app detects the controller and allows remapping

  Scenario: Switch controller profiles
    Given multiple controller profiles exist
    When the user selects a different profile
    Then the game uses the newly selected profile

  Scenario: Calibrate analog inputs
    Given a controller with analog inputs is connected
    When the user runs calibration
    Then the calibration values are saved for the controller
