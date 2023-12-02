#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """

import urllib
from urllib import request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with request.urlopen(url) as response:
        body = response.read()

        print(f"Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body.decode('utf-8')}")
        print(f"\t- utf8 content: {}".format(response_body.decode('utf-8')))

