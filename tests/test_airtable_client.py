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


def test_list_records_returns_200_and_non_empty_records(client):
    """Test that list_records returns a 200 response with records length > 0"""
    table_id = os.getenv("AIRTABLE_TEST_TABLE_ID")
    assert table_id, "AIRTABLE_TEST_TABLE_ID not found in .env"

    # Make the list_records request
    result = client.list_records(table=table_id)

    # Verify records exist and length is greater than 0
    assert "records" in result, "Response should contain 'records' key"
    assert isinstance(result["records"], list), "Records should be a list"
    assert len(result["records"]) > 0, "Records length should be greater than 0"


def test_list_fields_returns_non_empty_fields_list(client):
    """Test that list_fields returns a non-empty list of field dicts"""
    table_id = os.getenv("AIRTABLE_TEST_TABLE_ID")
    assert table_id, "AIRTABLE_TEST_TABLE_ID not found in .env"

    # Make the list_fields request
    fields_list = client.list_fields(table=table_id)

    # Verify a non-empty list of dicts is returned
    assert isinstance(fields_list, list), "list_fields should return a list"
    assert len(fields_list) > 0, "Fields list should be non-empty"
    assert all(isinstance(item, dict) for item in fields_list), "Each item should be a dict of fields"
