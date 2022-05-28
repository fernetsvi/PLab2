from threading import Thread
from WorkItem import WorkItem
from WorkerThread import WorkerThread


class CustomExecutor:
    def __init__(self, max_workers):
        self.max_workers = max_workers
        self.work = True
        self.thr = []
        self.queue = []

        if max_workers <= 0:
            raise ValueError("Number of workers can't be <= 0 !")
        for i in range(max_workers):
            self.thr.append(Thread(target=WorkerThread.run, args=[self], daemon=True))
            self.thr[-1].start()

    def execute(self, func, arg):
        item = WorkItem(func, arg)
        self.queue.append(item)
        return item

    def map(self, func, args_array):
        temp = []
        for arg in args_array:
            temp.append(self.execute(func, arg))
        return temp

    def shutdown(self):
        while True:
            if True in [i.future.hasResult for i in self.queue]:
                self.work = False
                [i.join() for i in self.thr]
                return

    def get(self):
        for i in self.queue:
            if not i.inWork:
                i.inWork = True
                return i
