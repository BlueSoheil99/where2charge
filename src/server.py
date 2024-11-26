# server.py
from fastapi import FastAPI
from typing import Dict
from logic import recommender as logic_handler

app = FastAPI()

# Sample data that might represent some geographical analysis
@app.get("/map_data")
async def get_map_data() -> Dict:
    data = {
        "locations": [
            {"name": "Location A", "lat": 47.6062, "lon": -122.3321},
            {"name": "Location B", "lat": 47.6097, "lon": -122.3331},
        ]
    }
    return data

@app.get("/get_suggestions")
async def get_suggestions(address) -> Dict:
    return logic_handler.get_suggestions(address)

