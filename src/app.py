# app.py
import streamlit as st
import requests
import folium
from streamlit_folium import st_folium

# Fetch map data from FastAPI server
def fetch_map_data():
    try:
        response = requests.get("http://localhost:8000/map_data")
        response.raise_for_status()
        return response.json().get("locations", [])
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return []

# Create Streamlit app layout
st.title("Interactive Map with Streamlit and FastAPI")

# Center map on Seattle, for example
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
