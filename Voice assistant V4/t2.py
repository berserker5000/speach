class Processor():
    def __init__(self, *commands):
        self.commands = commands

    def execute(self, text):
        k = 0
        for i in self.commands:
            if i.procent(text) == 1:
                k = i.execute(text)
                return k
            else:
                pass
        return k


# 1 - success, 0 - nothing to do, -1 - error

class RunProgram():
    def procent(self, text):
        if text == "open zoom":
            return 1
        elif text == "open jitsi":
            return 1

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
            return "Calling Vasya"
        return "not calling"


class Mail():
    def procent(self, text):
        if text == "mail dima":
            return 1
        elif text == "mail vasya":
            return 1
        else:
            return 0

    def execute(self, text):
        if text == "mail dima":
            return "Sending mail to Dima"
        elif text == "mail vasya":
            return "Sending mail to Vasya"
        else:
            return "nothing to send"


program = RunProgram()
program2 = RunProgram()
calling = Call()
mail = Mail()
processor = Processor(program, calling, mail, program2)

processor.execute("open zoom")
print
processor.execute("call dima")
print
processor.execute("open zoo")
print
processor.execute("mail dima")
print
processor.execute("open jitsi")
