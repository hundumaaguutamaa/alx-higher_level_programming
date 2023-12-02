#!/usr/bin/python3
"""Uses the GitHub API to display the user id."""

import requests
import sys

if __name__ == "__main__":
    # Replace 'YOUR_ACCESS_TOKEN' with your actual personal access token
    username = sys.argv[1]
    access_token = sys.argv[2]

    # URL for the authenticated user endpoint in GitHub API
    url = "https://api.github.com/user"

    # Set up the authentication using Basic Authentication with the access token
    auth = (username, access_token)

    # Send a GET request to the GitHub API with Basic Authentication
    response = requests.get(url, auth=auth)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        user_data = response.json()

        # Display the user id
        print(f"User ID: {user_data['id']}")
    else:
        print(f"Error: {response.status_code}. Unable to fetch user data.")
