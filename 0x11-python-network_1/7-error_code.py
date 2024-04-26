#!/usr/bin/python3
"""
Takes in a URL, ikohereza request to the URL, displays the body ya
response. Prints an error message if the HTTP status code is >= 400.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
