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
            try:
                text = self.inp.getText()
            except Exception:
                return "Sorry, we have faced with unexpected error." \
                       "\nProgramm will be closed."
            if text == "exit" or text == "quit":
                break
            self.processor.execute(text)
        return


def InputChoose():
    inp = Inputs()
    input_list = inp.getInputList()
    i = 0
    tmp = dict()
    print "You can use one of input type:"
    for name, object in input_list.iteritems():
        i += 1
        tmp[i] = name
        print i, name

    chosen_input = input("Please, enter what to use (enter just number):\n")
    try:
        return input_list[tmp[chosen_input]]
    except Exception:
        print "Error occurred. Program will be closed"
    return


processor = Processor(load_plugins(plugins_directory))
assistant = Assistant(processor, InputChoose())
assistant.start()