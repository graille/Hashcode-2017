# -*- coding: utf-8 -*-
from class.Cache import *
from class.Endpoint import *
from class.Video import *


import operator

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



    def run(self):
        print("Running...")
        self.calculateGains()
        print("Runned ! \n Populating cache...")
        self.solve()
        print("Sonved!\n Writing solutions....")
        self.writeSolutionFile()
        print("done !")


    def calculateGains(self):
        self.gains = []
        for videoID in videos:
            for (endpointID, req) in videoID.requests:
                for (cacheID:latency) in endpoint.latency:
                    self.gains.append(((endpointID, videoID, cacheID),videos[videoID].size*req*(endpoints[endpointID].dataCenterLatency-latency)))

        self.gains.sort(reverse=true, key=operator.itemgetter(1))

    def solve(self):
        #solution[cache_id(int)] = [video1, video5, ...(int)]
        self.solution = {}

        # List is sorted
        for element in self.gains:
            id_endpoint, id_video, id_cache = element[0]
            taille_video = this.videos[id_video].size
            if this.cache[id_cache].canAdd(taille_video):
                self.solution[id_cache].append(id_video)
                self.solution[id_cache].emptySpace -= taille_video
            # Si pas de place, prendre le prochain libre
            else:
                pass

    def writeSolutionFile(self):
        nCacheUsed = len(self.solution)
        with open(fileName, "a") as f:
            f.write(str(nCacheUsed)+'\n')

            for cache_id in self.solution.keys():
                line = str(cache_id)+' '
                for video_id in self.solution[cache_id]:
                    line += str(video_id)+' '
                f.write(line[:-1]+'\n')
