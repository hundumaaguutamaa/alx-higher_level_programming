#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """

from urllib import request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with request.urlopen(url) as response:
        response_body = response.read()

        print(f"Body response:")
        print(f"\t- type: {type(response_body)}")
        print(f"\t- content: {response_body.decode('utf-8')}")
        print(f"\t- utf8 content: {response_body.decode('utf-8')}")
