"""This module contains the tests for the googleAPI_handler module."""
import pytest
import pandas as pd
from where2charge.logic.googleAPI_handler import GoogleAPIHandler
from src import util

GOOGLE_API_KEY = util.read_config('src/config.yaml')['GOOGLE_API_KEY']
# Smoke test 1. Check if we get any output
def test_smoke():
    output = GoogleAPIHandler(GOOGLE_API_KEY)
    assert output is not None

# Smoke Test 2. the output type of the data
def test_output_type():
    output = GoogleAPIHandler(GOOGLE_API_KEY)
    assert type(output) == pd.DataFrame

# Smoke test 3. Check if we get any error
def test_smoke_error():
    with pytest.raises(Exception):
        GoogleAPIHandler(GOOGLE_API_KEY)

# Edge test 1. Check if it works with invalid data