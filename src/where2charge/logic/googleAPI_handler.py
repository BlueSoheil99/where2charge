""" this code will gather EVCS data from Google API.
implemented using OOP
"""

__all__=[]

from typing import Dict, List


def _get_locations_from_google(address: str) -> List[Dict]:
    """Get the locations of the given address using the Google Places API (text search).

    Args:
        address (str): The address to get the locations of.

    Returns:
        List[Dict]: A list of dictionaries containing the name, latitude, and longitude of each location.
    """
    return []


def _get_details_from_google(locations: List[Dict]) -> List[Dict]:
    """Get the details of the given locations using the Google Place API (place details api).

    Args:
        locations (List[Dict]): A list of dictionaries containing the name, latitude, and longitude of each location.

    Returns:
        List[Dict]: A list of dictionaries containing the details of each location.
    """
    return []


def _get_routes_from_google(locations: List[Dict]) -> List[Dict]:
    """Get the routes between the given locations using the Google Directions API.

    Args:
        locations (List[Dict]): A list of dictionaries containing the name, latitude, and longitude of each location.

    Returns:
        List[Dict]: A list of dictionaries containing the routes between each pair of locations.
    """
    return []

class GoogleAPIHandler:
    def __init__(self, api_key: str):
        print('google api handler is made')
        pass

    def get_locations(address: str) -> List[Dict]:
        """Get the locations of the given address using the Google Places API.

        Args:
            address (str): The address to get the locations of.

        Returns:
            List[Dict]: A list of dictionaries containing the name, latitude, and longitude of each location.
        """
        #todo: implement these functions

        locations = _get_locations_from_google(address)
        details = _get_details_from_google(locations)
        routes = _get_routes_from_google(locations)
        #todo: merge locations and details
        # one possible way of returning the data: {1: [dict_of_location1, dict_of_details1, dict_of_routes1], 2: [dict_of_location2, dict_of_details2, dict_of_routes2], ...}
        return locations


