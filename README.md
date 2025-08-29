# Smartphone Classes in Python

This project contains Python classes that model smartphones and gaming smartphones. It demonstrates key object-oriented programming concepts such as **encapsulation**, **inheritance**, and **polymorphism**.

## Files

- `smartphone.py` (or your filename): Contains the definition of the `Smartphone` base class and the `GamingSmartphone` subclass.

## Classes

### Smartphone

Represents a basic smartphone with the following attributes:

- `brand`: Manufacturer of the phone (e.g., Samsung).
- `model`: Model name or number (e.g., Galaxy S21).
- `storage_gb`: Internal storage capacity (encapsulated as a private attribute).
- `battery_mah`: Battery capacity in milliampere-hours.

#### Key Methods

- `describe()`: Returns a string describing the phone.
- `battery_life(screen_time_hours)`: Estimates remaining battery capacity after a number of hours of screen time.
- `get_storage()` and `set_storage()`: Getter and setter for the private storage attribute, ensuring controlled access.

### GamingSmartphone

Inherits from `Smartphone` and adds gaming-specific features:

- `cooling_system`: Describes the cooling technology (e.g., Liquid Cooling).
- `rgb_lighting`: Boolean indicating presence of RGB lighting.

#### Key Methods

- `describe()`: Extends the description to include gaming features.
- `game_performance(game_name)`: Simulates running a game at high settings.

## Usage Example

# Python-Week-5-Assignment
