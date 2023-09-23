#!/bin/env/python3
# This collector is written by Bosse Klein and is licensed under the APACHE
# 2.0 license
# This collector grabs all API issue endpoints from the Glitchtip API and
# exports them

import requests as req

# initialize variables

# initialize requests
session = req.Session()


def get_organizations(url, token):
    url_Suffix = '/api/0/organizations/'
    headers = {
        'Authorization': 'Basic ' + token,
        'Accept': 'application/json',
    }
    url = url + url_Suffix
    response = session.get(url, headers=headers)
    return response.json()


def get_enviroments_list(url, token, organization_slug):
    url_Suffix = '/api/0/organizations/' + organization_slug + '/environments/'
    headers = {
        'Authorization': 'Basic ' + token,
        'Accept': 'application/json',
    }
    url = url + url_Suffix
    response = session.get(url, headers=headers)
    return response.json()


def get_organizations_issues_list(url, token, organization_slug):
    # View and bulk update issues
    url_Suffix = '/api/0/organizations/' + organization_slug + '/issues/'
    headers = {
        'Authorization': 'Basic ' + token,
        'Accept': 'application/json',
    }
    url = url + url_Suffix
    response = session.get(url, headers=headers)
    return response.json()


def get_organizations_issues_tags(url, token, organization_slug, issue_id):
    # View and bulk update issues
    url_Suffix = '/api/0/organizations/' + organization_slug + '/issues/' + issue_id + '/tags/'
    headers = {
        'Authorization': 'Basic ' + token,
        'Accept': 'application/json',
    }
    url = url + url_Suffix
    response = session.get(url, headers=headers)
    return response.json()


def get_organizations_member_list(url, token, organization_slug):
    # View and bulk update issues
    url_Suffix = '/api/0/organizations/' + organization_slug + '/members/'
    headers = {
        'Authorization': 'Basic ' + token,
        'Accept': 'application/json',
    }
    url = url + url_Suffix
    response = session.get(url, headers=headers)
    return response.json()


def get_organizations_monitors_list(url, token, organization_slug):
    # View and bulk update issues
    url_Suffix = '/api/0/organizations/' + organization_slug + '/monitors/'
    headers = {
        'Authorization': 'Basic ' + token,
        'Accept': 'application/json',
    }
    url = url + url_Suffix
    response = session.get(url, headers=headers)
    return response.json()
