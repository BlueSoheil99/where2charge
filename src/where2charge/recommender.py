"""
This file get connected to the server and handles the logic
behind our work. To start working with this code, function 'establish_connection'
should be called after importing the module
"""

from .logic.googleAPI_handler import GoogleAPIHandler
from .logic.analyzer import Analyzer

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
    def __init__(self):
        self.analyzer = None
        self.google_handler = None


    def establish_connection(self, google_api_key, openai_api_key):
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
        except: #todo: exact error type and message TBD
            print('ERRRORRROORORO')


    def get_suggestions(self, address: str) -> dict:
        """

        :param address:
        :return:
        """
        #todo: check if ValueError makes sense to raise
        if self.google_handler is None:
            raise ValueError('Google API not established. Run "establish_connection" first')
        if self.analyzer is None:
            raise ValueError('Analyzer not established. Run "establish_connection" first')

        locations = self.google_handler.get_locations(address)
        # data = data_handler.get_data(locations)
        #todo: merge data with locations
        suggestions = self.analyzer.get_suggestions(locations)
        return suggestions  ## return JSON object containing suggestions
