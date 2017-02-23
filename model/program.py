class Program:
    def __init__(self):
        self.caches = []
        self.endpoints = []
        self.videos = []

    def addCache(self, cache):
        self.caches.append(cache)

    def addEndpoint(self, endpoint):
        self.endpoints.append(endpoint)

    def addVideos(self, video):
        self.videos.append(video)