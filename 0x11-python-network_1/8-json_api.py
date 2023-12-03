#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a letter as a parameter."""

import requests
import sys

if __name__ == "__main__":
    """ Sends a POST request to http://0.0.0.0:5000/search_user with a given letter."""
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    """ Create a dictionary (payload) with the letter as a parameter. """
    payload = {'q': q}

    """ Send a POST request to the specified URL. """
    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        """ Try to parse the JSON response. """
        json_response = response.json()

        """ Check if the JSON is properly formatted and not empty. """
        if json_response and isinstance(json_response, dict):
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")

