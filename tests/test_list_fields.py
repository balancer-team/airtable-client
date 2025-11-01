import os


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
