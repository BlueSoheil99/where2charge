""" this code will gather EVCS data from Google API.
implemented using OOP
"""
from typing import Dict, List
from datetime import datetime

import pandas as pd
import googlemaps
import livepopulartimes   # pip install --upgrade git+https://github.com/GrocerCheck/LivePopularTimes


__all__=['GoogleAPIHandler']


class GoogleAPIHandler:
    def __init__(self, api_key: str):
        self.gmaps = googlemaps.Client(key=api_key)
        self.API_KEY = api_key
        print('google api handler is made')
        # todo: add a check for the api key
    
    def get_charger_review_dataframe(self, latitude, longitude):
        data = []  # List to store data for the DataFrame

        # Perform a nearby search
        results = self.gmaps.places_nearby(
            location=(latitude, longitude), 
            keyword='EV charging station', 
            rank_by='distance'
        )

        if results.get('results'):
            for i, result in enumerate(results['results'], start=1):
                if i > 10:  # Limit to the top 10 results
                    break
                
                # Extract Place ID and station location
                place_id = result['place_id']
                station_location = f"{result['geometry']['location']['lat']},{result['geometry']['location']['lng']}"
                Latitude = result['geometry']['location']['lat']
                Longitude = result['geometry']['location']['lng']
                # review score
                review_score = result['rating']
                # number of people rated
                rating_count = result['user_ratings_total']
                # Fetch detailed information for the place
                details = self.gmaps.place(place_id=place_id)

                # Extract reviews
                reviews = []
                if 'reviews' in details['result']:
                    for review in details['result']['reviews']:
                        reviews.append(f"{review['author_name']}: {review['text']}")
                else:
                    reviews.append("No reviews found.")

                # Get distances and travel times
                distance_result = self.gmaps.distance_matrix(
                    origins=(latitude, longitude),
                    destinations=station_location,
                    mode="driving",  
                    departure_time="now",  # Real-time traffic
                    traffic_model="best_guess"  # Options: "optimistic", "pessimistic", "best_guess"
                )

                if distance_result['rows'][0]['elements'][0]['status'] == 'OK':
                    distance = distance_result['rows'][0]['elements'][0]['distance']['text']
                    duration = distance_result['rows'][0]['elements'][0]['duration_in_traffic']['text']
                else:
                    distance = "N/A"
                    duration = "N/A"
                
                # Extract route
                route_result = self.gmaps.directions(
                    origin=(latitude, longitude), 
                    destination=station_location, 
                    mode="driving", 
                    departure_time="now", 
                    traffic_model="best_guess"
                )
                route = route_result[0] if route_result else "No route found."

                # Make the data
                data.append({
                    "Name": result['name'],
                    "Location": result['geometry']['location'],
                    "Latitude": Latitude,
                    "Longitude": Longitude,
                    "Place_ID": place_id,
                    "Review score": review_score,
                    "Rating count": rating_count,
                    "Reviews": reviews,
                    "Distance": distance,
                    "Travel_Time": duration,
                    "Route": route  # Store the route details here
                })
        else:
            print("No results found.")

        # Convert the data to a pandas DataFrame
        df = pd.DataFrame(data)
        return df


    def get_all_data_from_google(self, latitude, longitude):
        """This function will add popular times data to the DataFrame. However, the popular times data is only available for a limited number of places. 
        Another issue is that LivePopularTimes is not an official Google API, so it may not be as reliable as the official Google API. It is not also working properly 
        for some of the location and cannot scrape their popular times data while it is available on Google Maps.
        """
        # Initialize the Google Maps client
        df = self.get_charger_review_dataframe(latitude, longitude)
        df['Popular_times'] = None
        df['Popular_moment'] = None
        for i in range(len(df)): # we might have less than 10 in the previous function
            place_id = df.loc[i, 'Place_ID'] 
            #Get the popular times data
            popular_times = livepopulartimes.get_populartimes_by_PlaceID(self.API_KEY, place_id)
            if popular_times['popular_times'] is None:
                popular_moment = 'not_known'
            else:
                popular_moment = livepopulartimes.get_populartimes_by_PlaceID(self.API_KEY, place_id)['populartimes'][datetime.today().isoweekday() -1]['data'][datetime.today().hour]
            df.loc[i, 'Popular_times'] = str(popular_times)
            df.loc[i, 'Popular_moment'] = popular_moment
        return df