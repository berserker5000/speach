import time


class GeneralProgransExecutor():
    def executor(self, text):
        pass

    def get_current_time(self):
        return time.strftime("%A %d of %b %Y year %H hours %M minutes")

    def procentCount(self, text):
        splited_text = text.split(" ")
        counter = 0
        if "time" in text:
            counter = 1
        return counter
