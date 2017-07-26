import time


class GetTimeExecutor():
    def executor(self, text):
        return time.strftime("%A %d of %b %Y year %H hours %M minutes")

    def procentCount(self, text):
        counter = 0
        if "time" in text:
            counter = 1
        return counter

    def nothingCanDo(self):
        pass