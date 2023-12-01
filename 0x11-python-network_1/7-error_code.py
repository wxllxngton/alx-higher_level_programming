#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL
and displays the body of the response.
"""

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) != 2:
        print(f"Usage: ./{sys.argv[0]} 'url'")
        exit(1)

    url = sys.argv[1]

    r = requests.get(url=url)
    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)
