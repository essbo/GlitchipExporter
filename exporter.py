#!/bin/env/python3

import glitchtip
import prometheus_client as prom
import base64
import json
import pickle as rick
import requests
import pycurl
import argparse
import yaml


# initialize arguments
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--config', help='path to config file')
parser.add_argument('-p', '--port', help='port to listen on')
parser.add_argument('-t', '--target', help='target to send events to')
parser.add_argument('-u', '--username', help='username for target')
parser.add_argument('-P', '--password', help='password for target')
parser.add_argument('-v', '--verbose', help='verbose output')
parser.add_argument('-d', '--debug', help='debug output')
parser.add_argument('-f', '--filter', help='filter events')
parser.add_argument('-l', '--labels', help='labels to add to events')
parser.add_argument('-m', '--metrics', help='metrics to export')
parser.add_argument('-g', '--group', help='group events')
parser.add_argument('-r', '--regex', help='regex to match events')
parser.add_argument('-a', '--alert', help='alert events')
parser.add_argument('-n', '--namespace', help='namespace for metrics')
parser.add_argument('-b', '--buckets', help='buckets for histograms')
parser.add_argument('-k', '--key', help='key for metrics')
parser.add_argument('-e', '--event', help='event to send')

args = parser.parse_args()





# inizitialize prometheus and metrics
prom.start_http_server(8000)
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
