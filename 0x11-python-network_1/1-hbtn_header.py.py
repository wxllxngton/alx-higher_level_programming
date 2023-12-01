#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""

if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.error

    # Checks to see if argument was passed
    if len(sys.argv) != 2:
        print(f"Usage: ./{sys.argv[0]} 'url'")
        exit(1)

    url = sys.argv[1]
    try:
        req = urllib.request.Request(url=url)
        with urllib.request.urlopen(req) as response:
            headers = response.info()
            x_request_id = headers.get("X-Request-Id")
            if x_request_id:
                print(x_request_id)
            else:
                print("X-Request-Id not found in the response headers.")
    except urllib.error.URLError as e:
        print(f"Error accessing the URL: {e}")
