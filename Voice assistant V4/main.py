import pyttsx

from LoadInputs import *
from LoadPlugins import *
from SysInfo import SystemInformation

sysinfo = SystemInformation()

'''
Each module MUST have nothingCanDo, execute, procentCount
procentCount should return 0 - if can't do anything with request, 1 - if can make everything.
nothingCanDo should return text with explanation why can't execute process
execute should return executed process and run what it must
'''


class Speaker(object):
    def __init__(self, language="english"):
        self.engine = pyttsx.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)
        self.engine.setProperty('voice', language)
        self.engine.setProperty('rate', 150)

    def speak(self, text):
        self.engine.say(text)
        return self.engine.runAndWait()


class Processor(object):
    def __init__(self, commands):
        self.commands = commands

    def execute(self, text):
        for element in self.commands:
            if element.procentCount(text) == 1:
                return element.execute(text)
        return


class Assistant(object):
    def __init__(self, processor, inp):
        self.processor = processor
        self.inp = inp

    def start(self):
        while True:
            text = self.inp.getText()
            if text == "exit":
                break
            self.processor.execute(text)
        return


processor = Processor(load_plugins(plugins_directory))

inp = Inputs()
print "You can use one of input type:"
for name, object in inp.getInputList().iteritems():
    print name
chosen_input = raw_input("Please, enter what to use:\n")
assistant = Assistant(processor, inp.getInputList()[chosen_input])
assistant.start()