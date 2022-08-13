# tinder-tracker

This is a project that shows how one could use [Pynder](https://github.com/charliewolf/pynder) to potentially trace users on Tinder.

Detailed documentation/discussion about this project can be found [here](https://essentialistengineer.com/can-a-tinder-account-be-traced/).

## Usage

### `tinder_people_finder.py`

Can be used to search for Tinder users by name and age in a specified location.

The script will print the user ID, name, and a list of the users image urls.

### `tinder_distance_finder.py`

This script will print the distance from a specified location to a given user, identified via its user ID.

Given three geolocation points (lat/lon) and their respective distance to a given user, one could use a trilateration method to calculate the exact location of a given user.

## Installation

    python -m pip install git+https://github.com/charliewolf/pynder.git@5d2104d21cdea6ad07166a45c3e91864113d6e3e
