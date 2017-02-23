# -*- coding: utf-8 -*-

class Endpoint:
    def __init__(self, id, dataCenterLatency = None, latency = None, requests = None):
        self.id = id
        self.dataCenterLatency = dataCenterLatency

        self.latency = latency # dict : cache:latency
        self.requests = requests #dict : video:req
