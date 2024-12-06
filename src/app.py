"""
client side implemented with Streamlit
"""
import sys
import requests

import folium
import streamlit as st
from streamlit_folium import st_folium


# initiating default and fixed values
DEFAULT_TIMEOUT = 5
MAP_CENTER = [47.6062, -122.3321] # Center map on Seattle
server_port = sys.argv[1]
DEFAULT_RECOMS = 5

# initiating session states
if "origin" not in st.session_state:
    st.session_state["origin"] = []
if "markers" not in st.session_state:
    st.session_state["markers"] = []
if 'find_button_disabled' not in st.session_state:
    st.session_state["find_button_disabled"] = True
if 'find_button_label' not in st.session_state:
    st.session_state["find_button_label"] = 'select a point on map'
if 'origin_variable' not in st.session_state:
    st.session_state["origin_variable"] = True


@st.cache_data
def fetch_map_data(location, num_recommendations):
    """

    :param location:
    :param num_recommendations:
    :return:
    """
    lat, lng = location
    try:
        response = requests.get(
            f"http://localhost:{server_port}/get_suggestions/?lat={lat}&lng={lng}&n={num_recommendations}",
            timeout=DEFAULT_TIMEOUT
        )
        response.raise_for_status()
        print(response.text)
        return response.json().get("locations", [])
    except requests.exceptions.Timeout:
        print("Request timed out")
        return []
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return []


def clear_map():
    """
    we tried to call it with clear_button. NO success
    :return:
    """
    st.session_state["origin"] = []
    st.session_state["markers"] = []
    st.session_state['find_button_label'] = f'select a point on map'
    st.session_state["find_button_disabled"] = False
    st.session_state["origin_variable"] = True


# Create Streamlit app layout
st.title("where2charge")
st.subheader('An EV charging station recommender')

### this button works well if we place it here and not after making the map
# if st.button("Add random marker"):
#     import random
#     random_lat = random.random() * 0.5 + 39.8
#     random_lon = random.random() * 0.5 - 75.2
#     random_marker = folium.Marker(
#         location=[random_lat, random_lon],
#         popup=f"Random marker at {random_lat:.2f}, {random_lon:.2f}",
#     )
#     st.session_state["markers"].append(random_marker)


m = folium.Map(location=MAP_CENTER, zoom_start=12)
fg = folium.FeatureGroup(name="Markers")

if len(st.session_state["origin"])>0:
    fg.add_child(st.session_state["origin"][0])
for marker in st.session_state["markers"]:
    fg.add_child(marker)

# m.add_child(folium.ClickForMarker())

st_folium_map = st_folium(
    m,
    key="map",
    feature_group_to_add=fg,
    height=400,
    width=700,
)


find_button = st.button(st.session_state['find_button_label'], disabled=st.session_state["find_button_disabled"])
num_recoms = st.slider("How many recommendations to provide?", 1, 10, DEFAULT_RECOMS)

if st_folium_map["last_clicked"]:
    # print(f'st_folium_map["last_clicked"]: {st_folium_map["last_clicked"]}')
    if st.session_state["origin_variable"]:
        point = st_folium_map["last_clicked"]
        marker = folium.Marker(
            location=[point['lat'], point['lng']],
            popup=f"{point['lat']}, {point['lng']}",
            tooltip=f"{point['lat']}, {point['lng']}",
            icon=folium.Icon(color="red")
        )
        st.session_state["origin"] = [marker]
        st.session_state['find_button_label']= f'find nearest charging stations for {point}'
        st.session_state["find_button_disabled"] = False


if find_button:
    locations = fetch_map_data(st.session_state["origin"][0].location, num_recoms)
    print(locations)
    st.session_state["markers"] = []
    st.session_state["origin_variable"] = False

    for loc in locations:
        marker = folium.Marker(
            location=[loc["lat"], loc["lon"]],
            popup=loc["name"],
            tooltip=loc["name"]
        )
        st.session_state["markers"].append(marker)

if not st.session_state["origin_variable"]:
    # clear_button = st.button('clear search', callable(clear_map)) #todo callable not working
    clear_button = st.button('clear search')
    if clear_button:
        # clear_map()
        st.session_state["origin"] = []
        st_folium_map["last_clicked"] = None
        #todo this line is not working well
        # print(f'st_folium_map["last_clicked"] after making it none: {st_folium_map["last_clicked"]}')
        st.session_state["markers"] = []
        st.session_state['find_button_label'] = f'select a point on map'
        st.session_state["find_button_disabled"] = True
        st.session_state["origin_variable"] = True

    # download_button = st.download_button('download data', locations)
    #     st.rerun()

