#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""

import sys
import requests


if __name__ == "__main__":
    """ get the url from the command line """ 
    url = sys.argv[1]
    email = sys.argv[2]

    """ create an email  dictionary"""
    e_data = {'email': email}

    # send a POST request to the URL
    response = requests.post(url, data=e_data)
    print(response.text)

