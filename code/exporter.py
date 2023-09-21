#!/bin/env/python3
# This exporter is written by Bosse Klein and is licensed under the APACHE 2.0 license
# This Exporter grabs all API Endpoint metrics from the Glitchtip API and exports them
# to a scrapable prometheus endpoint.



from prometheus_client import Counter, Histogramm, Gauge, Summary, start_http_server as prom
from prometheus_client import multiprocess as pc_multiprocess, CollectorRegistry as prom_reg
import base64 as b64
import json as js
import pickle as rick
import requests as req
import pycurl as curl
import argparse as arg
import yaml
import sys 
import time as t
import configparser as cfg
import os
import threading as thrd
import pathlib as path
import inspect 
import functools 
import re
import logging as log


# initialize arguments
parser = arg.ArgumentParser()

parser.add_argument('-c', '--config', help='path to config file', default='config.yaml')
parser.add_argument('-v', '--verbose', help='increase output verbosity', action='store_true')
parser.add_argument('-p', '--port', help='port to run exporter on', default=9999)
parser.add_argument("-l", "--log", dest="logLevel", choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], help="Set the logging level")
parser.add_argument("-b", "--bind", dest="bind", help="Set the ip-address for the server to run on", default='0.0.0.0')
parser.add_argument("-s", "--scrape", dest="scrape", help="Set the scrape interval in seconds", default=15)
parser.add_argument("-t", "--threads", dest="threads", help="Set the number of threads to run", default=2)
parser.add_argument("-c", "--collector", dest="collector", help="Set the collector to run", default='all')
parser.add_argument("-d", "--debug", dest="debug", help="Set the debug mode", default=False)

args = parser.parse_args()





# inizitialize prometheus and metrics
prom.start_http_server(9999)
metric = prom.Gauge('metric', 'metric description', ['label1', 'label2'])
metric.set(0, ['label1value', 'label2value'])


# initialize glitchtip
glitchtip.init('http://localhost:3000', 'test', 'test')
# initialize curl
curl = pycurl.Curl()
curl.setopt(pycurl.VERBOSE, 1)
curl.setopt(pycurl.URL, 'http://localhost:3000/api/v1/events')
curl.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json'])
curl.setopt(pycurl.POST, 1)
curl.setopt(pycurl.USERPWD, 'test:test')
curl.setopt(pycurl.POSTFIELDS, '')
