# -*- coding: utf-8 -*-

class Cache:
    def __init__(self, id, capacity, latency = {}):
        self.id = id
        self.emptySpace = capacity
        self.latency = latency
        self.videos = {}

    def canAdd(self, tailleVideo):
        return self.emptySpace - tailleVideo >= 0
