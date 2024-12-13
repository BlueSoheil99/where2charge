""" Tests for the server module. """
import pytest
from src.server import Recommender

# edge test. Empty API keys
def test_recommender_with_empty_keys():
    """
    Test Recommender initialization with empty API keys.
    """
    google_api_key = ""
    openai_api_key = ""

    with pytest.raises(ValueError, match="Invalid API key provided. API key must be a non-empty string."):
        _ = Recommender(google_api_key, openai_api_key)
