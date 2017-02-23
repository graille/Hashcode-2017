# -*- coding: utf-8 -*-
from entity.Cache import *
from entity.Endpoint import *
from entity.Video import *


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
        for video in self.videos:
            for (endpointID, req) in video.requests.items():
                for (cacheID, latency) in self.endpoints[endpointID].latency.items():
                    self.gains.append(((endpointID, video.id, cacheID), video.size * req * (self.endpoints[endpointID].dataCenterLatency - latency)))

        self.gains.sort(reverse=True, key=operator.itemgetter(1))

    def solve(self):
        #solution[cache_id(int)] = [video1, video5, ...(int)]
        self.solution = {cacheId:[] for cacheId in range(len(self.caches))}

        # List is sorted
        for element in self.gains:
            id_endpoint, id_video, id_cache = element[0]
            taille_video = self.videos[id_video].size
            if self.caches[id_cache].canAdd(taille_video):
                self.solution[id_cache].append(id_video)
                self.caches[id_cache].emptySpace -= taille_video
            # Si pas de place, prendre le prochain libre
            else:
                pass

    def writeSolutionFile(self):
        nCacheUsed = len(self.solution)
        with open('output.txt', "w") as f:
            f.write(str(nCacheUsed)+'\n')

            for cache_id in self.solution.keys():
                if self.solution[cache_id] != []:
                    line = str(cache_id)+' '
                    for video_id in self.solution[cache_id]:
                        line += str(video_id) + ' '
                    f.write(line[:-1]+'\n')
