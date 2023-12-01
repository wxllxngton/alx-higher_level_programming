#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

if __name__ == "__main__":
    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"

    payload = dict(q=sys.argv[1]) if len(sys.argv) == 1 else dict(q="")

    r = requests.post(url=url, data=payload)

    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print(response)
            print(
                "[{}] {}".format(
                    response.get("id", "N/A"), response.get("name", "N/A")
                )
            )
    except ValueError:
        print("Not a valid JSON")
