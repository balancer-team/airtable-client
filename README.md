# Airtable Python Client

A simple Python client for interacting with the Airtable API.

### Install

You can install the package via pip:

```bash
pip install airtable-client
```

### Usage

Here's a basic example of how to use the Airtable client:

```python
from airtable_client import AirtableClient
base = AirtableClient(api_key='your_api_key', base_id='your_base_id')
records = base.list_records('table_name_or_id')
print(records)
```
