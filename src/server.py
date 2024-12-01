""" running a server using fastAPI library.
    Make sure you have valid keys for Google Places and OpenAI APIs in the config file."""

from typing import Dict

from fastapi import FastAPI

from .where2charge.recommender import Recommender
from . import util

app = FastAPI()

GPT_API_KEY = util.read_config('src/config.yaml')['OpenAI_API_KEY']
GOOGLE_API_KEY = util.read_config('src/config.yaml')['GOOGLE_API_KEY']
logic_handler = Recommender()
logic_handler.establish_connection(GOOGLE_API_KEY, GPT_API_KEY)


@app.get("/map_data")
async def get_map_data() -> Dict:
    """
    test function
    :return:
    """
    data = {
        "locations": [
            {"name": "Location A", "lat": 47.6062, "lon": -122.3321},
            {"name": "Location B", "lat": 47.6097, "lon": -122.3331},
        ]
    }
    return data

@app.get("/get_suggestions")
async def get_suggestions(address) -> Dict:
    """
    Might be the main function. In development...
    :param address:
    :return:
    """
    return logic_handler.get_suggestions(address)
