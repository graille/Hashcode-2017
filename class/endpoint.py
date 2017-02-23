class Endpoint:
    def __init__(self, id, dataCenterLatency):
        self.id = id
        self.dataCenterLatency = dataCenterLatency

        self.latency = [] # item i contains latency of i cache
        self.requests = [] #item i contains nb of requets for video i
