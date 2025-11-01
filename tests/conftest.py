import os
import pytest
from dotenv import load_dotenv
from src.airtable_client import AirtableBase


@pytest.fixture
def client():
    """Create an AirtableBase using environment variables from .env"""
    load_dotenv()
    api_key = os.getenv("AIRTABLE_API_KEY")
    base_id = os.getenv("AIRTABLE_TEST_BASE_ID")

    assert api_key, "AIRTABLE_API_KEY not found in .env"
    assert base_id, "AIRTABLE_TEST_BASE_ID not found in .env"

    return AirtableBase(api_key=api_key, base_id=base_id)
