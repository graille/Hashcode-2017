class Program:
    def __init__(self):
        self.caches = []
        self.endpoints = []
        self.videos = []

        self.nbVideos = 0
        self.nbCache = 0
        self.nbEndpoint = 0
        self.cacheCapacity = float(inf)

    def addCache(self, cache):
        self.caches.append(cache)

    def addEndpoint(self, endpoint):
        self.endpoints.append(endpoint)

    def addVideos(self, video):
        self.videos.append(video)