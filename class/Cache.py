class Cache:
    def __init__(self, id, capacity):
        self.id = id
        self.capacity = capacity

        self.latency = [] #item i contains latency of cache i

        self.videos = [] #store the id of videos stored in the cache


    def addVideos(self, newVideos):
        pass
