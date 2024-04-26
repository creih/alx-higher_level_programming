#!/usr/bin/python3
"""
Takes in a URL, ikohereza request to the URL, and displays the value of the
variable X-Request-Id muri response header.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
