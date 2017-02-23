# -*- coding: utf-8 -*-

class Video:
    def __init__(self, id, size = None, requests = {}):
        self.id = id
        self.size = size

        self.requests = requests #dict : endpoint:req

        self.cache = {} #dict
