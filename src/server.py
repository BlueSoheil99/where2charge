"""
running a server using fastAPI library.
Make sure you have valid keys for Google Places and OpenAI APIs in the config file.
"""

import json
from typing import Dict

from fastapi import FastAPI

from .where2charge.recommender import Recommender
from . import util

app = FastAPI()

GPT_API_KEY = util.read_config('src/config.yaml')['OpenAI_API_KEY']
GOOGLE_API_KEY = util.read_config('src/config.yaml')['GOOGLE_API_KEY']
logic_handler = Recommender(GOOGLE_API_KEY, GPT_API_KEY)


@app.get("/get_suggestions")
async def get_suggestions(lat, lng, n=5, type=None) -> Dict:
    """
    Main function. Gets suggestions from our package
    :param lat: latitude
    :param lng: longitude
    :param n: number of recommendations
    :return: data in JSON format
    """
    lat, lng, n = float(lat), float(lng), int(n)
    print(f'asked for {n} recommendations')
    data = logic_handler.get_suggestions(lat, lng, n, type)
    data = json.loads(data)
    return data


