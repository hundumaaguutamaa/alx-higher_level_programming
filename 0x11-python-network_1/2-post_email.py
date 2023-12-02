#!/usr/bin/python3
""" Sends a POST request to a given URL with a given email. """
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data_encoded = urllib.parse.urlencode(value).encode("ascii")
    
    request = urllib.request.Request(url, data_encoded)
    with urllib.request.urlopen(request) as response:
        """ Printing decoded utf file"""
        print(response.read().decode("utf-8"))

