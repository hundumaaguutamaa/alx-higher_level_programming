#!/usr/bin/python3
""" Please list 10 commits (from the most recent to oldest) of the repository. """
import sys
import requests


if __name__ == "__main__":
    """ Constructs the URL for the GitHub API endpoint that provides
        information about the commits of a specified repository
    """
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"

    """  Sends a GET request to the GitHub API using the constructed URL
    """
    store_r = requests.get(url)
    commits = store_r.json()

    try:
        for i in range(10):
            """ Prints information about each commit. """
            print(f"{commits[i].get('sha')}: {commits[i].get('commit').get('author').get('name')}")

