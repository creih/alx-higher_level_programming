#!/usr/bin/python3
"""
Takes GitHub usrnm and personal access token as arguments and uses Basic
Authentication with the GitHub API to display the user ID.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'

    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_data = response.json()
        print(user_data['id'])
    else:
        print(None)
