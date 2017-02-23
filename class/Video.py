# -*- coding: utf-8 -*-


class Video:
    def __init__(self, id, size, requests):
        self.id = id
        self.size = size

        self.requests = requests #dict

        self.cache = {} #dict
