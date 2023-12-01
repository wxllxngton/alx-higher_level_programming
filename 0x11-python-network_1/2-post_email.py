#!/usr/bin/python3
"""
Script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse
    import urllib.error

    # Checks to see if arguments were passed
    if len(sys.argv) != 3:
        print(f"Usage: ./{sys.argv[0]} 'url' 'email'")
        exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    values = {"email": email}
    data = urllib.parse.urlencode(values).encode("ascii")

    try:
        req = urllib.request.Request(url=url, data=data)
        with urllib.request.urlopen(req) as response:
            content = response.read()
            print(content.decode("utf-8"))
    except urllib.error.URLError as e:
        print(f"Error accessing the URL: {e}")
