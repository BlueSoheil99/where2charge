""" This module contains tests for the TextAnalyzer class in the text_analyzer module. """
import pytest
import pandas as pd
from src.where2charge.logic.text_analyzer import TextAnalyzer
from src import util

OpenAI_API_KEY = util.read_config('src/config.yaml')['OpenAI_API_KEY']
# Smoke test 1: Check if we get any output
def test_smoke():
    """Smoke test for the TextAnalyzer class."""
    analyzer = TextAnalyzer(api_key=OpenAI_API_KEY)
    assert analyzer is not None
    assert isinstance(analyzer, TextAnalyzer) 

#Edge test 1: Invalid API Key Raises ValueError
def test_invalid_api_key():
    """Test the TextAnalyzer class with an invalid API key."""
    with pytest.raises(
        ValueError, match="Invalid API key provided. API key must be a non-empty string."
        ):
        TextAnalyzer(api_key="")  # Empty API key


# Edge test 2: Invalid Input Data Type Raises TypeError
def test_invalid_input_data_type():
    """Test the TextAnalyzer class with invalid input data type"""
    analyzer = TextAnalyzer(api_key = OpenAI_API_KEY)
    with pytest.raises(TypeError, match="Input data must be a Pandas DataFrame."):
        analyzer.LLM_analyze(data="not_a_dataframe")  # Passing string instead of DataFrame


# Edge test 3: Missing Columns in DataFrame Raises RuntimeError
def test_missing_columns_in_dataframe():
    """Test the TextAnalyzer class with missing columns in the DataFrame."""
    analyzer = TextAnalyzer(api_key= OpenAI_API_KEY)
    invalid_data = {
        "Review score": [4.5, 3.0],
        "Rating count": [10, 5]
    }  # Missing 'Location', 'Reviews', 'Travel_Time'
    invalid_df = pd.DataFrame(invalid_data)

    with pytest.raises(RuntimeError, match="Failed to process DataFrame. Check the input format."):
        analyzer.LLM_analyze(data=invalid_df)
