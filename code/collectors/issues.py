#!/bin/env/python3
# This collector is written by Bosse Klein and is licensed under the
# APACHE 2.0 license
# This collector grabs all API issue endpoints from the Glitchtip API and
# exports them

import requests as req

# initialize variables

# initialize requests
session = req.session()


# Get IDs and Tags of all issues
#
def get_issues(url, token):
    # View and bulk update issues
    url_Suffix = '/api/0/issues/'
    headers = {
        'Authorization': 'Bearer ' + token,
        'Accept': 'application/json',
    }
    url = url + url_Suffix
    response = session.get(url, headers=headers)
    return response.json()


def get_issue_tags(url, token, issue_id):
    # View and bulk update issues
    url_Suffix = '/api/0/issues/' + issue_id + '/tags/'
    headers = {
        'Authorization': 'Bearer ' + token,
        'Accept': 'application/json',
    }
    url = url + url_Suffix
    response = session.get(url, headers=headers)
    return response.json()

# Get Details of a single issue
#


def get_issue(url, token, issue_id):
    # View and bulk update issues
    url_Suffix = '/api/0/issues/' + issue_id
    headers = {
        'Authorization': 'Bearer ' + token,
        'Accept': 'application/json',
    }
    url = url + url_Suffix
    response = session.get(url, headers=headers)
    return response.json()


def get_issue_tag(url, token, issue_id, tag_id):
    # View and bulk update issues
    url_Suffix = '/api/0/issues/' + issue_id + '/tags/' + tag_id
    headers = {
        'Authorization': 'Bearer ' + token,
        'Accept': 'application/json',
    }
    url = url + url_Suffix
    response = session.get(url, headers=headers)
    return response.json()


# Run Collector
#
def run_collector(url, token):
    # Get all issues
    issues = get_issues(url, token)
    for issue in issues:
        # Get all tags of an issue
        issue_tags = get_issue_tags(url, token, issue['id'])
        for issue_tag in issue_tags:
            # Get details of a single issue
            issue_details = get_issue(url, token, issue['id'])
            # Get details of a single tag
            issue_tag_details = get_issue_tag(url, token, issue['id'],
                                              issue_tag['tag'])
            # Export data to file

    return issues, issue_tags, issue_details, issue_tag_details


# initialze main function
#
def main(url, token):
    return run_collector(url, token)


# This is the main entry point for the collector
#
if __name__ == "__main__":
    print(main())
