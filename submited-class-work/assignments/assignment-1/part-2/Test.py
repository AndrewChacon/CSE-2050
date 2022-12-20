import unittest
from Task import Task
from TaskQueue import TaskQueue

class TaskTest(unittest.TestCase):

    def test_init(self):
        t = Task(1, 3)

    def test_init(self):
        t = Task(1, 3)
        self.assertEqual(t.reduce_time, 2)

class TaskQueueTest(unittest.TestCase):

    def test_init(self):
        tq = TaskQueue()

    def test_length(self):
        tq = TaskQueue()
        self.assertEqual(tq.__len__(), 0)

    def test_is_empty(self):
        tq = TaskQueue()
        self.assertEqual(tq.is_empty(), True)

    def test_add_task(self):
        t1 = Task(1, 3)
        tasks = [t1]
        TQ = TaskQueue()
        for task in tasks:
            TQ.add_task(task)
        self.assertEqual(TQ.is_empty(), False)

    def test_remove_task(self):
        t1 = Task(1, 3)
        t2 = Task(2, 1)
        t3 = Task(3, 5)
        tasks = [t1, t2, t3]
        TQ = TaskQueue()
        for task in tasks:
            TQ.add_task(task)
        TQ.remove_task(1)
        self.assertEqual(TQ.__len__(), 2)

    def test_execute_tasks(self):
        t1 = Task(1, 3)
        t2 = Task(2, 1)
        t3 = Task(3, 5)
        tasks = [t1, t2, t3]
        TQ = TaskQueue()
        for task in tasks:
            TQ.add_task(task)
        TQ.execute_tasks()
        pass
        self.assertEqual(TQ.__len__(), 2)

        

# if (__name__ == '__main__'):
    # unittest.main()


t1 = Task(1, 3)
t2 = Task(2, 1)
t3 = Task(3, 5)
tasks = [t1, t2, t3]
TQ = TaskQueue()
for task in tasks:
    TQ.add_task(task)

# TQ.remove_task(1)
TQ.execute_tasks()