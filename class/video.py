class Video:
    def __init__(self, id, size):
        self.id = id
        self.size = size

        self.requests = [] #item i contains requests at endpoint i
