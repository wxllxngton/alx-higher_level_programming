#!/usr/bin/python3
"""
Script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) != 3:
        print(f"Usage: ./{sys.argv[0]} 'url' 'email'")
        exit(1)

    url = sys.argv[1]
    payload = dict(email=sys.argv[2])

    try:
        r = requests.post(url=url, data=payload)
        r.raise_for_status()  # Raises an HTTPError for bad responses
        content = r.text
        print(content)
    except requests.RequestException as e:
        print(f"Error accessing the URL: {e}")
