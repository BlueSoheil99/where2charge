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
    # return logic_handler.get_suggestions(lat, lng, n)
    lat, lng = float(lat), float(lng)
    print(f'asked for {n} recommendations')
    data = {
        "locations": [
            {"name": "Location A", "lat": lat+random.random()/100, "lon": lng+random.random()/100},
            {"name": "Location B", "lat": lat+random.random()/100, "lon": lng+random.random()/100},
        ],
        "query_status": f'successful with {n} recommendations'
    }
    return data
