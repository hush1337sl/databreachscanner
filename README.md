# Email Lookup Script

This Python script uses the IPQualityScore API to check if a given email address has been exposed in leaked data. The output is color-coded for better readability.

## Prerequisites

- Python 3.x
- `requests` library
- `colorama` library

## Installation

1. Clone the repository or download the files.
2. Install the required Python libraries with `pip`:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:

    ```sh
    python email_lookup.py
    ```

2. Enter the email address you want to look up when prompted.

## Example

```
Enter an email to look up: example@example.com
Email was detected in leaked data
{
    "success": true,
    "message": "Success",
    "request_hash": "8f3a31910452145aabb670b02163cc7f7d15442b210d5cfc2ccd7e9c69ffd294",
    "source": [
        "You must be Enterprise or higher to view the leak sources"
    ],
    "exposed": true,
    "first_seen": {
        "human": "just now",
        "timestamp": 1718960462,
        "iso": "2024-06-21T05:01:02-04:00"
    },
    "request_id": "OSVaT4tEy6"
}
