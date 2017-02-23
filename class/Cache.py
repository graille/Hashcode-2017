# -*- coding: utf-8 -*-

class Cache:
    def __init__(self, id, capacity, latency):
        self.id = id
        self.capacity = capacity

        self.latency = latency #item i contains latency of cache i

        self.videos =  #store the id of videos stored in the cache
