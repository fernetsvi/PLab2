class FutureResult:
    def __init__(self):
        self.res = None
        self.hasResult = False

    def setResult(self, res):
        self.res = res
        self.hasResult = True

    def result(self):
        while not self.hasResult:
            pass
        return self.res
