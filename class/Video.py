# -*- coding: utf-8 -*-


class Video:
    def __init__(self, id, size, requests):
        self.id = id
        self.size = size

        self.requests = requests #item i contains requests at endpoint i

        self.cache[] #contains the id of caches where the video will be stored
