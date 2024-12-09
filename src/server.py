"""
running a server using fastAPI library.
Make sure you have valid keys for Google Places and OpenAI APIs in the config file.
"""

import random
from typing import Dict

from fastapi import FastAPI

from .where2charge.recommender import Recommender
from . import util

app = FastAPI()

GPT_API_KEY = util.read_config('src/config.yaml')['OpenAI_API_KEY']
GOOGLE_API_KEY = util.read_config('src/config.yaml')['GOOGLE_API_KEY']
logic_handler = Recommender()
logic_handler.establish_connection(GOOGLE_API_KEY, GPT_API_KEY)


@app.get("/get_suggestions")
async def get_suggestions(lat, lng, n=5) -> Dict:
    """
    Main function. Gets suggestions from our package
    :param lat: latitude
    :param lng: longitude
    :param n: number of recommendations
    :return: data in JSON format
    """
    lat, lng = float(lat), float(lng)
    # return logic_handler.get_suggestions(lat, lng, n)
    lat1, lng1 = lat+random.random()/100, lng+random.random()/100
    lat2, lng2 = lat+random.random()/100, lng+random.random()/100
    print(f'asked for {n} recommendations')
    data = {
        "locations": [
            {"name": "Location A", "lat": lat1, "lon": lng1, "route": [(lat, lng),(lat1, lng1)], "duration":5},
            {"name": "Location B", "lat": lat2, "lon": lng2, "route": get_routes(), "duration":3}
        ],
        "query_status": f'successful with {n} recommendations'
    }

    return data

def get_routes():
    data = {'bounds': {'northeast': {'lat': 47.6072982, 'lng': -122.3364654}, 'southwest': {'lat': 47.6061238, 'lng': -122.3378607}}, 'copyrights': 'Map data Â©2024 Google', 'legs': [{'distance': {'text': '0.1 mi', 'value': 233}, 'duration': {'text': '1 min', 'value': 60}, 'duration_in_traffic': {'text': '1 min', 'value': 59}, 'end_address': '1201 2nd Ave, Seattle, WA 98101, USA', 'end_location': {'lat': 47.606449, 'lng': -122.3378607}, 'start_address': '1223 2nd Ave, Seattle, WA 98101, USA', 'start_location': {'lat': 47.6072982, 'lng': -122.33711}, 'steps': [{'distance': {'text': '305 ft', 'value': 93}, 'duration': {'text': '1 min', 'value': 17}, 'end_location': {'lat': 47.60658489999999, 'lng': -122.3364654}, 'html_instructions': 'Head <b>southeast</b> on <b>2nd Ave</b> toward <b>Seneca St</b>', 'polyline': {'points': 'shqaH|}tiVfB}APOTQ'}, 'start_location': {'lat': 47.6072982, 'lng': -122.33711}, 'travel_mode': 'DRIVING'}, {'distance': {'text': '318 ft', 'value': 97}, 'duration': {'text': '1 min', 'value': 31}, 'end_location': {'lat': 47.6061238, 'lng': -122.3375617}, 'html_instructions': 'Turn <b>right</b> at the 1st cross street onto <b>Seneca St</b>', 'maneuver': 'turn-right', 'polyline': {'points': 'cdqaH|ytiVBJL^x@fCNd@'}, 'start_location': {'lat': 47.60658489999999, 'lng': -122.3364654}, 'travel_mode': 'DRIVING'}, {'distance': {'text': '141 ft', 'value': 43}, 'duration': {'text': '1 min', 'value': 12}, 'end_location': {'lat': 47.606449, 'lng': -122.3378607}, 'html_instructions': 'Turn <b>right</b> onto <b>1st Ave</b><div style="font-size:0.9em">Destination will be on the right</div>', 'maneuver': 'turn-right', 'polyline': {'points': 'gaqaHv`uiVa@\\_@\\'}, 'start_location': {'lat': 47.6061238, 'lng': -122.3375617}, 'travel_mode': 'DRIVING'}], 'traffic_speed_entry': [], 'via_waypoint': []}], 'overview_polyline': {'points': 'shqaH|}tiVxBmBTQBJfAfDNd@a@\\_@\\'}, 'summary': '2nd Ave and Seneca St', 'warnings': [], 'waypoint_order': []}
    coordinates = []

    for leg in data["legs"]:
        for step in leg["steps"]:
            coordinates.append((step["start_location"]["lat"], step["start_location"]["lng"]))
            coordinates.append((step["end_location"]["lat"], step["end_location"]["lng"]))
    return coordinates

