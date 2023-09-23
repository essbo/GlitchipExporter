#!/bin/env/python3
# This exporter is written by Bosse Klein and is licensed under the APACHE 2.0 license
# This Exporter grabs all API Endpoint metrics from the Glitchtip API and exports them
# to a scrapable prometheus endpoint.



from prometheus_client import Counter, Histogramm, Gauge, Summary, start_http_server as prom
from prometheus_client import multiprocess as pc_multiprocess, CollectorRegistry as prom_reg
import base64 as b64
import json as js
import requests as req
import pycurl as curl
import argparse as arg
import yaml
import sys 
import time as t
import threading as thrd
import pathlib as path
import inspect 
import functools 
import re
import systemd.journal import JounaldLogHandler as jlh
import logging
from logging.handlers import TimedRotatingFileHandler as tpfh
from collectors import issues, list, projects, users, organizations, teams

# initialize variables

value_issue = {}
value_list = {}
value_projects = {}
value_users = {}
value_organizations = {}
value_teams = {}

# initialize arguments
parser = arg.ArgumentParser()

parser.add_argument('-c', '--config',
                    help='path to config file',
                    default='config.yaml')

parser.add_argument('-v',
                    '--verbose',
                    help='increase output verbosity',
                    action='store_true')

parser.add_argument('-p',
                    '--port',
                    help='port to run exporter on',
                    default=9999)

parser.add_argument("-l",
                    "--log",
                    dest="logLevel",
                    choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                    help="Set the logging level")

parser.add_argument("-b",
                    "--bind",
                    dest="bind",
                    help="Set the ip-address for the server to run on",
                    default='0.0.0.0')

parser.add_argument("-s",
                    "--scrape",
                    dest="scrape",
                    help="Set the scrape interval in seconds",
                    default=15)

parser.add_argument("-d",
                    "--debug",
                    dest="debug",
                    help="Set the debug mode",
                    default=False)

args = parser.parse_args()


# initialize logging journal
logger = logging.getLogger(__name__)
logger.setLevel(args.logLevel)
journal_handler = jlh.JournalHandler()
logger.addHandler(journal_handler)
logger.propagate = False
journal_handler.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))
logger.addHandler(journal_handler)

# initialize logging file
logger = logging.getLogger(__name__)
logger.setLevel(args.logLevel)
handler = tpfh('/var/log/glitchtip_exporter.log', when='midnight', interval=1, backupCount=7)
logger.addHandler(handler)

# import config.yml

with open(args.config, 'r') as config:
    config = yaml.load(config, Loader=yaml.FullLoader)


# inizitialize prometheus and metrics
metric = prom.Gauge('metric', 'metric description', ['label1', 'label2'])
metric.set(0, ['label1value', 'label2value'])

# initialize collectors
class issuesThread(thrd.Thread):
    def __init__(self):
        thrd.Thread.__init__(self)
        self.value = None
    def run(self):
        issues.run()
        self.dict1 = issues.dict1
        self.dict2 = issues.dict2
        self.dict3 = issues.dict3

class listThread(thrd.Thread):
    def __init__(self):
        thrd.Thread.__init__(self)
        self.value = None
    def run(self):
        list.run()
        self.dict1 = list.dict1
        self.dict2 = list.dict2
        self.dict3 = list.dict3

class projectsThread(thrd.Thread):
    def __init__(self):
        thrd.Thread.__init__(self)
        self.value = None
    def run(self):
        projects.run()
        self.dict1 = projects.dict1
        self.dict2 = projects.dict2
        self.dict3 = projects.dict3

class usersThread(thrd.Thread):
    def __init__(self):
        thrd.Thread.__init__(self)
        self.value = None
    def run(self):
        users.run()
        self.dict1 = users.dict1
        self.dict2 = users.dict2
        self.dict3 = users.dict3

class organizationsThread(thrd.Thread):
    def __init__(self):
        thrd.Thread.__init__(self)
        self.value = None
    def run(self):
        organizations.run()
        self.dict1 = organizations.dict1
        self.dict2 = organizations.dict2
        self.dict3 = organizations.dict3

class teamsThread(thrd.Thread):
    def __init__(self):
        thrd.Thread.__init__(self)
        self.value = None
    def run(self):
        teams.run()
        self.dict1 = teams.dict1
        self.dict2 = teams.dict2
        self.dict3 = teams.dict3


# initialize threads
issuesThread = issuesThread()
listThread = listThread()
projectsThread = projectsThread()
usersThread = usersThread()
organizationsThread = organizationsThread()
teamsThread = teamsThread()

# start threads

