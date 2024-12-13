"""This module contains the tests for the data_handler module."""
import pytest
import pandas as pd
from src.where2charge.logic.data_handler import get_supplementary_data

ADR_PRE = 'src/where2charge/logic'
# Smoke tests 1. Check if we get any output
def test_smoke():
    """Smoke test for the get_supplementary_data function."""
    output = get_supplementary_data(address_prefix=ADR_PRE, generate=True)
    assert output is not None

# Smoke Test 2 (or One-shot tests). the output type
def test_output_type():
    """Test the output type of the get_supplementary_data function."""
    output = get_supplementary_data(address_prefix=ADR_PRE)
    assert isinstance(output, pd.DataFrame)
# Edge tests 1. Check if it works with invalid data
def test_invalid_input():
    """Test the get_supplementary_data function with invalid input"""
    invalid_input = []
    with pytest.raises(Exception):
        get_supplementary_data._get_geo_data(invalid_input)

# Edge tests 2. Check if it works with invalid data columns
def test_invalid_input_columns():
    """Test the get_supplementary_data function with invalid input columns"""
    invalid_geo_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    invalid_df_ev = pd.DataFrame({'C': [1, 2, 3], 'D': [4, 5, 6]})
    with pytest.raises(Exception):
        get_supplementary_data._merge_data(invalid_geo_df, invalid_df_ev)
