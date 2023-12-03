#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """

 from urllib.request import urlopen

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    """ fetch the url """
     with urlopen("https://alx-intranet.hbtn.io/status") as response:
        response_body = response.read()

        """ Display response body with tabulation """
        print(f"Body response:")
        print(f"\t- type: {type(response_body)}")
        print(f"\t- content: {response_body.decode('utf-8')}")
        print(f"\t- utf8 content: {response_body.decode('utf-8')}")
