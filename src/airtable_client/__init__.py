import requests
import time

BASE_URL = "https://api.airtable.com/v0"


class AirtableClient:
    def __init__(self, api_key: str, base_id: str):
        self.api_key = api_key
        self.base_id = base_id
        self.base_url = f"{BASE_URL}/{self.base_id}"
        self.headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        self.last_request_time = 0
        self.min_request_interval = 0.2  # 5 requests per second = 0.2 seconds between requests

    def _rate_limit(self):
        """Ensure we don't exceed 5 requests per second"""
        current_time = time.time()
        time_since_last_request = current_time - self.last_request_time
        if time_since_last_request < self.min_request_interval:
            time.sleep(self.min_request_interval - time_since_last_request)
        self.last_request_time = time.time()

    def list_records(self, table_id_or_name: str, fields: list[str] | None = None, view: str | None = None):
        """
        Fetch all records from a table using a POST request to avoid URL length limits.
        - If fields is a list, only those fields are returned.
        - If fields is None or empty, all fields are returned.
        - If view is specified, only records in that view are returned.
        """
        url = f"{self.base_url}/{table_id_or_name}/listRecords"
        rows = []
        offset = None

        # Build the base payload for the request body
        payload = {}
        if fields:
            payload["fields"] = fields
        if view:
            payload["view"] = view

        while True:
            self._rate_limit()  # Apply rate limiting before each request

            # Add offset to payload for pagination
            if offset:
                payload["offset"] = offset

            response = requests.post(url, headers=self.headers, json=payload)
            response.raise_for_status()
            data = response.json()

            # Extract the 'fields' dictionary from each record
            for record in data.get("records", []):
                rows.append(record.get("fields", {}))

            offset = data.get("offset")
            if not offset:
                break
        return rows
