class Processor():
    def __init__(self, *commands):
        self.commands = commands

    def execute(self, text):
        for i in self.commands:
            if i.procent(text) == 1:
                print i.execute(text)
            else:
                print "no"
        return


class RunProgram():
    def procent(self, text):
        if text == "open zoom":
            return 1
        elif text == "open jitsi":
            return 1
        else:
            return 0

    def execute(self, text):
        if text == "open zoom":
            return "runing zoom"
        elif text == "open jitsi":
            return "runing jitsi"
        else:
            return "nothing to run"


class Call():
    def procent(self, text):
        if text == "call dima":
            return 1
        elif text == "call vasya":
            return 1
        else:
            return 0

    def execute(self, text):
        if text == "call dima":
            return "Calling Dima"
        elif text == "call vasya":
            return "Calling Vsya"
        else:
            return "not calling"


program = RunProgram()
calling = Call()
processor = Processor(program, calling)

print processor.execute("open zoom")
print processor.execute("call dima")
print processor.execute("open zoo")
