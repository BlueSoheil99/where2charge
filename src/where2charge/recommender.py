"""
This file get connected to the server and handles the logic
behind our work. To start working with this code, function 'establish_connection'
should be called after importing the module
"""
import geopandas as gpd
from shapely.geometry import Point

from .logic.googleAPI_handler import GoogleAPIHandler
from .logic.analyzer import Analyzer
from .logic.data_handler import get_supplementary_data


class Recommender:
    """
    In order to make suggestion to EV users, we need to have a logic handler that
    controls and mixes all different parts of the logic. Therefore, one connection
    to openai api and one connection to google Places api is needed. Since using
    global variables is not popular and recommended, the alternative is to switch
    to object-oriented programming (OOP).

    In our new design, the user may need to instantiate a recommender object in
    which there are other objects that need to be in working status first.
    These objects are: a data collection object, a Google api handler object,
    and an analyzer object.
    """
    def __init__(self, google_api_key, openai_api_key):
        """
        the recommendation system can work when analyzer and google api connections
        can work.
        :param google_api_key:
        :param openAI_api_key:
        :return:
        """
        try:
            self.analyzer = Analyzer(openai_api_key)
            self.google_handler = GoogleAPIHandler(google_api_key)
            self.evcs_data = get_supplementary_data()
        except Exception as e: #todo: exact error type and message TBD
            print(f'Error: {e}')


    def get_suggestions(self, lat, lng, n_recomm) -> dict:
        """

        :param address:
        :return:
        """
        # if self.google_handler is None:
        #     raise ValueError('Google API not established. Run "establish_connection" first')
        # if self.analyzer is None:
        #     raise ValueError('Analyzer not established. Run "establish_connection" first')

        google_data = self.google_handler.get_all_data_from_google(lat, lng)
        data = self._merge_data(google_data, self.evcs_data)
        # suggestions = self.analyzer.get_suggestions(data)
        #todo: send only first n_recommendations
        # return suggestions.to_json()  ## return JSON object containing suggestions
        data.to_csv('data.csv')
        return data.to_json()  ## return JSON object containing suggestions

    

    def _merge_data(self, google_data, evcs_data):
        """
        merge the data from google and evcs"""
        # Convert to GeoDataFrame
        gdf10 = gpd.GeoDataFrame(google_data, geometry=gpd.points_from_xy(google_data['Longitude'], google_data['Latitude']))
        gdf_all = gpd.GeoDataFrame(evcs_data, geometry=gpd.points_from_xy(evcs_data['Longitude'], evcs_data['Latitude']))

        # Create buffer
        buffer_size = 0.0001   # buffer size might be problematic
        gdf10['buffer'] = gdf10.geometry.buffer(buffer_size)

        # Drop or rename conflicting columns
        gdf10 = gdf10.drop(columns=['index_left', 'index_right'], errors='ignore')
        gdf_all = gdf_all.drop(columns=['index_left', 'index_right'], errors='ignore')

        # Perform spatial join
        merged = gpd.sjoin(gdf10.set_geometry('buffer'), gdf_all, how='inner', predicate='intersects')

        # Cleanup and finalize
        result = merged.drop(columns=['buffer']).reset_index(drop=True)
        return result
