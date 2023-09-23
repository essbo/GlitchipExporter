#!/bin/env/python3
# This collector is written by Bosse Klein and is licensed under the APACHE
# 2.0 license
# This collector grabs all API issue endpoints from the Glitchtip API and
# exports them

import requests as req

# initialize variables

# initialize requests
session = req.session()


def get_subscriptions(url, token):
    url_Suffix = '/api/0/subscriptions/'
    headers = {
        'Authorization': 'Basic ' + token,
        'Accept': 'application/json',
    }
    url = url + url_Suffix
    response = session.get(url, headers=headers)
    return response.json()