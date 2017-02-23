class Endpoint:
    def __init__(self, id, dataCenterLatency):
        self.id = id
        self.dataCenterLatency = dataCenterLatency

        self.caches = {} # dict of : cache:latency (ms)
