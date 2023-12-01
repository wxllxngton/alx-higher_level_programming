#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse
    import urllib.error

    # Checks to see if arguments were passed
    if len(sys.argv) != 2:
        print(f"Usage: ./{sys.argv[0]} 'url'")
        exit(1)

    url = sys.argv[1]

    try:
        req = urllib.request.Request(url=url)
        with urllib.request.urlopen(req) as response:
            content = response.read()
            print(content.decode("utf-8"))
    except urllib.error.URLError as e:
        print(f"Error code: {e.code}")
