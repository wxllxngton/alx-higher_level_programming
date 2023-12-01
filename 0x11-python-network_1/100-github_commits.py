#!/usr/bin/python3
"""
Script that takes your GitHub credentials (username and password) and
uses the GitHub API to list 10 commits (from the most recent to oldest)
of the repository “rails” by the user
"""

if __name__ == "__main__":
    import requests
    import sys

    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1]
    )

    r = requests.get(url=url)
    commits = r.json()

    try:
        for i in range(10):
            print(
                "{}: {}".format(
                    commits[i].get("sha"),
                    commits[i].get("commit").get("author").get("name"),
                )
            )
    except IndexError:
        pass
