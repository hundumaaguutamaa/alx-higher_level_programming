#!/usr/bin/python3
"""using requests module to fetch"""

import requests

if __name__ == "__main__":
    fetched = requests.get('https://alx-intranet.hbtn.io/status')

    print("Body response:")
    print(f"\t- type: {type(fetched.text)}")
    print(f"\t- content: {fetched.text}")

