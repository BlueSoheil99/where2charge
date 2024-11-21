# server.py
from fastapi import FastAPI
from typing import Dict

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
