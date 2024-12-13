"""This module contains the tests for the googleAPI_handler module."""
import pytest
import pandas as pd
from src.where2charge.logic.googleAPI_handler import GoogleAPIHandler
from src import util

GOOGLE_API_KEY = util.read_config('src/config.yaml')['GOOGLE_API_KEY']
# Smoke tests 1. Check if we get any output
def test_smoke():
    """Smoke test for the GoogleAPIHandler class."""
    client = GoogleAPIHandler(GOOGLE_API_KEY)
    assert client is not None

# Smoke Test 2. the output type of the data
def test_output_type():
    """Test the output type"""
    client = GoogleAPIHandler(GOOGLE_API_KEY)
    output = client.get_all_data_from_google(
        latitude=47.616303606504985, longitude=-122.32454538345338
        )
    assert isinstance(output, pd.DataFrame)


# Edge test 1. Inserting an invalid API key
def test_invalid_api_key():
    """Test the GoogleAPIHandler class with an invalid API key."""
    with pytest.raises(
        ValueError, match="Invalid API key provided. API key must be a non-empty string."
        ):
        GoogleAPIHandler("")

# Edge test 2. Inserting an invalid latitude and longitude (out of range)
def test_invalid_lat_long_range():
    """Test the GoogleAPIHandler class with invalid latitude and longitude range."""
    client = GoogleAPIHandler(GOOGLE_API_KEY)
    with pytest.raises(
        ValueError, match="Latitude and longitude must be within"
        " the range of -90 to 90 and -180 to 180"
        ):
        client.get_nearby_chargers_with_reviews_and_traveltimes(latitude=100, longitude=200)

# Edge test 3. Inserting an invalid latitude and longitude (not numeric)
def test_invalid_lat_long_format():
    """Test the GoogleAPIHandler class with invalid latitude and longitude format."""
    client = GoogleAPIHandler(GOOGLE_API_KEY)
    with pytest.raises(ValueError, match="Latitude and longitude must be numeric."):
        client.get_nearby_chargers_with_reviews_and_traveltimes(
            latitude=47.616303606504985, longitude="120.009218"
            )
