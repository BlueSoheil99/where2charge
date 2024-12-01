"""
client side implemented with Streamlit
"""
import sys
import requests

import folium
import streamlit as st
from streamlit_folium import st_folium


DEFAULT_TIMEOUT = 5

def fetch_map_data():
    """
    test function
    :return:
    """
    try:
        response = requests.get(f"http://localhost:{server_port}/map_data", timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()
        return response.json().get("locations", [])
    except requests.exceptions.Timeout:
        print("Request timed out")
        return []
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return []

# Create Streamlit app layout
server_port = sys.argv[1]
st.title("where2charge")
st.subheader('An EV charging station recommender')

# Center map on Seattle
map_center = [47.6062, -122.3321]
map_obj = folium.Map(location=map_center, zoom_start=12)

# Get data from FastAPI and add markers to the map
locations = fetch_map_data()
for loc in locations:
    folium.Marker(
        location=[loc["lat"], loc["lon"]],
        popup=loc["name"],
        tooltip=loc["name"]
    ).add_to(map_obj)

# Render the map in Streamlit
st_folium(map_obj, width=700, height=500)
