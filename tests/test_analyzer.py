"""This module contains the tests for the analyzer module."""
import pandas as pd

from src.where2charge.logic.analyzer import Analyzer
from src import util


# smoke test
def test_analyzer_and_LLM_smoke():
    """ Smoke test for the Analyzer class and the LLM_analyze method. """
    df = pd.read_csv('tests/test_data/data_google.csv')
    GPT_API_KEY = util.read_config('src/config.yaml')['OpenAI_API_KEY']
    connector_type = None
    n_recommendations = 5

    analyzer = Analyzer(GPT_API_KEY)
    df = analyzer.get_suggestions(df, n_recommendations, connector_type)
    assert True  # happens when no error is thrown
