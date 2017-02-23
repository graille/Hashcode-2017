# -*- coding: utf-8 -*-
from class.Cache import *
from class.Endpoint import *
from class.Video import *


class Program:
    def __init__(self):
        self.caches = []
        self.endpoints = []
        self.videos = []

        self.nbVideos = 0
        self.nbCaches = 0
        self.nbEndpoints = 0
        self.cacheCapacity = float("inf")

    def addCache(self, cache):
        self.caches.append(cache)

    def addEndpoint(self, endpoint):
        self.endpoints.append(endpoint)

    def addVideos(self, video):
        self.videos.append(video)


    def calculateGains(self):
        self.gains = {}
        for v 
