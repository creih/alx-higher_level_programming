#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL, and displays the value of the
X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header = response.headers.get('X-Request-Id')
        print(header)
