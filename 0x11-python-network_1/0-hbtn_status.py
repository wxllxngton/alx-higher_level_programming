#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using urllib
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.error

    try:
        with urllib.request.urlopen(
            "https://alx-intranet.hbtn.io/status"
        ) as res:
            content = res.read()
            print("Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(content.decode("utf-8")))
    except urllib.error.URLError as e:
        print(f"Error accessing the URL: {e}")
