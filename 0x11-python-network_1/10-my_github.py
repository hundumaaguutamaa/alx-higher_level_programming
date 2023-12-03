#!/usr/bin/python3
"""Uses the GitHub API to display the user id."""

import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    # Replace 'YOUR_ACCESS_TOKEN' with your actual personal access token
    username = sys.argv[1]
    password = sys.argv[2]

    # URL for the authenticated user endpoint in GitHub API
    url = 'https://api.github.com/user'

    # Set up the authentication using Basic Authentication with the access token
    auth = HTTPBasicAuth(username, password)

    # Send a GET request to the GitHub API with Basic Authentication
    response = requests.get(url, auth=auth)

        # Display the user id
    print(response.json().get("id"))
