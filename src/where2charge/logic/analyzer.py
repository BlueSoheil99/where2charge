""" this code will use all the data to suggest the best EV charging stations.
implemented using OOP
"""

__all__=[]

from .text_analyzer import TextAnalyzer


class Analyzer:
    """
    an analyzer object, uses data collected from Google and other data sources
    to find the best charging station. To do this, it also uses the help of
    ChatGPT
    """
    def __init__(self, openai_key):
        self.text_analyzer = TextAnalyzer(openai_key)
        print('analyzer is made and connected to openai')



    def get_suggestions(self, data, n_recomm, charger_type):
        """
        The main method. all data must be passed to this method
        :param data:
        :return:
        """
        # use text analyzer to get suggestions
        ans = []
        return data
