from FutureResult import FutureResult


class WorkItem:
    def __init__(self, func, arg):
        self.func = func
        self.arg = arg
        self.inWork = False
        self.future = FutureResult()

