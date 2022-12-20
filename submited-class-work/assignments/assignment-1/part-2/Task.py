class Task:
    def __init__(self, id: int, time_left: int):
        self.id = id
        self.time_left = time_left
        self.next = None
        self.prev = None

    def reduce_time(self):
        self.time_left = self.time_left - 1
        return self.time_left

