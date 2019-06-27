#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


class MetricsClient(object):
    """Single entry point to the metrics API"""
    token = ''
    auth_headers = {}

    def __init__(self, api_endp, auth_endp='', auth_user='', auth_pass=''):
        self.api_endp = api_endp
        self.events_endp = '%s/events' % (self.api_endp)
        self.measures_endp = '%s/measures' % (self.api_endp)
        if all([auth_endp, auth_user, auth_pass]):
            self.load_token(auth_endp, auth_user, auth_pass)

    def load_token(self, auth_endp, auth_user, auth_pass):
        self.token = self.get_token(auth_endp, auth_user, auth_pass)
        self.auth_headers = {'Authorization': 'Bearer %s' % (self.token)}

    def get_token(self, url, email, password):
        credentials = dict(email=email, password=password)
        auth = tuple(email, password)
        response = self.post_request(url, payload=credentials, auth=auth)
        return response[0]['token']

    def new_event(self, measure_uri, timestamp, work_uri, country_uri,
                  event_uri, value):
        payload = dict(measure_uri=measure_uri,
                       timestamp=timestamp,
                       work_uri=work_uri,
                       country_uri=country_uri,
                       event_uri=event_uri,
                       value=value)
        return self.post_request(self.events_endp, payload)

    def get_request(self, url):
        r = requests.get(url)
        if r.status_code != requests.codes.ok:
            raise ValueError(r.text)
        return r.json()['data']

    def post_request(self, url, payload={}, auth=()):
        r = requests.post(url, json=payload, headers=self.auth_headers,
                          auth=auth)
        if r.status_code != requests.codes.ok:
            raise ValueError(r.text)
        return r.json()['data']
