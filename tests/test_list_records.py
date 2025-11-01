import os


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
