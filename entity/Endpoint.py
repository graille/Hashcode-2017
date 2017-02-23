# -*- coding: utf-8 -*-

class Endpoint:
    def __init__(self, id, dataCenterLatency = None, latency = {}, requests = {}):
        self.id = id
        self.dataCenterLatency = dataCenterLatency
        self.latency = latency
        self.requests = requests
