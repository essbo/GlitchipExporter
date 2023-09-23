#!/bin/env/python3
# This collector is written by Bosse Klein and is licensed under the APACHE
# 2.0 license
# This collector grabs all API issue endpoints from the Glitchtip API and
# exports them

import requests as req
import json

# initialize variables

# initialize requests
session = req.Session()


# Initialize the functions
def get_list(url, token):
    headers = {
        'Authorization': 'Basic ' + token,
        'Accept': 'application/json',
    }
    url_Suffix = '/api/0/'
    url = url + url_Suffix
    response = session.get(url, headers=headers)
    return response.json()


def run_collector(url, token):
    # Turn Json into Dict
    data = json.loads(get_list(url, token))

    return data


# Initialize the main function
def main(url, token):
    return run_collector(url, token)


# This is the main entry point for the collector
if __name__ == "__main__":
    print(main())
