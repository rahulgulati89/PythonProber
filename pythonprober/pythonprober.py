#!/usr/bin/env python
  

import logging
import functools
import argparse
import time
import requests
from prometheus_client import Gauge, start_http_server
import threading
import datetime
g = Gauge('sample_external_url_up', 'URL Up/Down', ['url'])
h = Gauge('sample_external_url_response_ms', 'Response time', ['url'])
urllist = ['https://httpstat.us/200','https://httpstat.us/503']
def get_status_code():
  update_metrics(reschedule=True)
def update_metrics(reschedule=False):
  for urlstring in urllist:
    response = requests.get(urlstring, timeout=10)
    status_code = response.status_code
    elapsed_time = response.elapsed.microseconds/1000
    if status_code == 200:
      g.labels(url=urlstring).set(1)
      h.labels(url=urlstring).set(elapsed_time)
    else:
      g.labels(url=urlstring).set(0)
      h.labels(url=urlstring).set(elapsed_time)
  if reschedule:
    threading.Timer(30.0, get_status_code).start()
if __name__ == '__main__':
    start_http_server(7000)
    get_status_code()
