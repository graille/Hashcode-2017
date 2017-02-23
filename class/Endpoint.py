# -*- coding: utf-8 -*-



class Endpoint:
    def __init__(self, id, dataCenterLatency, latency, requests):
        self.id = id
        self.dataCenterLatency = dataCenterLatency

        self.latency = latency # item i contains latency of i cache
        self.requests = requests #item i contains nb of requets for video i
