#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from client import MetricsClient

METRICS_API_ENDP = os.getenv('METRICS_API_ENDP')
METRICS_AUTH_ENDP = os.getenv('METRICS_AUTH_ENDP')
METRICS_API_USER = os.getenv('METRICS_API_USER')
METRICS_API_PASS = os.getenv('METRICS_API_PASS')
AUTH = (METRICS_AUTH_ENDP, METRICS_API_USER, METRICS_API_PASS)

if not METRICS_API_ENDP:
    raise KeyError("You need to set 'METRICS_API_ENDP'.")

# we allow either all auth details or none
if not all([False if i and not all(AUTH) else True for i in AUTH]):
    raise KeyError("Found some authentication details, but not all.")


def initialise_service():
    return MetricsClient(api_endp=METRICS_API_ENDP,
                         auth_endp=METRICS_AUTH_ENDP,
                         auth_user=METRICS_API_USER,
                         auth_pass=METRICS_API_PASS)
