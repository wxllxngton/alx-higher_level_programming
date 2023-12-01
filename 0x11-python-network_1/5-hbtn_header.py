#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header
"""

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) != 2:
        print(f"Usage: ./{sys.argv[0]} 'url'")
        exit(1)

    url = sys.argv[1]

    try:
        r = requests.get(url=url)
        r.raise_for_status()  # Raises an HTTPError for bad responses
        headers = r.headers
        print(
            headers.get(
                "X-Request-Id",
                "X-Request-Id not found in the response headers.",
            )
        )
    except requests.RequestException as e:
        print(f"Error accessing the URL: {e}")
