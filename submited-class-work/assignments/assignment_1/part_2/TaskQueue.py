class Task:
    def __init__(self, id: int, time_left: int):
        self.id = id
        self.time_left = time_left
        self.next = None
        self.prev = None

    def reduce_time(self):
        self.time_left = self.time_left - 1
        return self.time_left


class TaskQueue:
    def __init__(self):
        self.current = None
        self.time_per_task = 1
        self.length = 0;

    def __len__(self):
        return self.length

    def is_empty(self):
        return True if self.current == None else False

    def add_task(self, task):
        # update to show an increment in length
        self.length = self.length + 1
        # On empty task queue
        if self.current == None:
            self.current = task
            self.current.next = self.current
            self.current.prev = self.current
        else:
            # When task queue is not empty
            task.next = self.current
            task.prev = self.current.prev
            self.current.prev.next = task
            self.current.prev = task

    def remove_task(self, task_id):
        # check if task queue is empty
        if self.current is None:
            raise Exception('Task queue is actually empty')
        elif self.current.id == task_id:
            if self.current.next == self.current:  
                self.current = None
                self.length = self.length - 1
            else:
                self.current.prev.next = self.current.next
                self.current.next.prev = self.current.prev
                self.current = self.current.next
                self.length = self.length - 1
        else:
            # grab current task as a temp value
            current_task = self.current.next
            while current_task != self.current:
                if current_task.id == task_id:
                    current_task.prev.next = current_task.next
                    current_task.next.prev = current_task.prev
                    self.length = self.length - 1
                current_task = current_task.next
            raise Exception('The task id ', task_id,' not in TaskQueue')
            # update to show a decrement in length

    def execute_tasks(self):
        # total up the time of running tasks
        time_counter = 0
        while not self.is_empty():
            current_task = self.current
            for sec in range(self.time_per_task):
                # if theres no time left, we remove the task since its finished
                if current_task.time_left == 0:
                    self.remove_task(current_task.id)
                    time_elapsed = time_counter + sec
                    print('Finished task ',current_task.id,' at t = ',time_elapsed,' seconds')
                else:
                    # time is still left so we keep working on the task
                    current_task.reduce_time()
                    time_counter = time_counter + 1
            if current_task.time_left != 0:
                self.current = self.current.next
        print('time =', time_counter)
        return time_counter