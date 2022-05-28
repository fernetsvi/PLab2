from threading import Thread


class WorkerThread(Thread):
    def run(queue):
        while True:
            item = queue.get()
            if not item is None:
                result = item.func(item.arg)
                item.future.setResult(result)
            if queue.work == False:
                return
