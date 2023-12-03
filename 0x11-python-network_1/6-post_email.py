#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter"""

import sys
import requests

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

    # Get the URL and email from the command line
    url = sys.argv[1]
    email = sys.argv[2]

    # Create an email dictionary
    e_data = {'email': email}

    # Send a POST request to the URL
    response = requests.post(url, data=e_data)

    # Print the response text
    print(response.text)
    
