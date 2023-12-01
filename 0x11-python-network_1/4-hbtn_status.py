#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status using requests
"""

if __name__ == "__main__":
    import requests

    try:
        r = requests.get("https://alx-intranet.hbtn.io/status")
        r.raise_for_status()  # Raises an HTTPError for bad responses
        content = r.text

        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
    except requests.RequestException as e:
        print(f"Error accessing the URL: {e}")
