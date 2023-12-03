#!/usr/bin/python3
""" Uses urllib to send requests. """

from urllib import request
import sys

if __name__ == "__main__":
    """ Get the URL from the command line argument """
    url = sys.argv[1]

    """ Make a GET request to the URL. """
    with request.urlopen(url) as response:
        x_request_id = response.getheader("X-Request-Id")
        if x_request_id:
            print(x_request_id)
        else:
            print("X-Request-Id not found in the response header.")

