#!/usr/bin/python3
""" Using request module to send a request to the URL. """


import requests
import sys


if __name__ == "__main__":
    """ Get the URL from the command line argument. """
    url = sys.argv[1]

    """Make a GET request to the URL. """
    get_response = requests.get(url)
    print(get_response.headers.get('X-Request-Id'))

