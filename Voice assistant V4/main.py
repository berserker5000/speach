import imp
import os
import sys

import pyttsx
# import speech_recognition as sr

from SysInfo import SystemInformation

sysinfo = SystemInformation()
cur_dir = os.path.dirname(os.path.abspath(__file__))
plugins_directory = cur_dir + "/Plugins"
inputs_directory = cur_dir + "/Inputs"

'''
Each module MUST have nothingCanDo, execute, procentCount
procentCount should return 0 - if can't do anything with request, 1 - if can make everything.
nothingCanDo should return text with explanation why can't execute process
execute should return executed process and run what it must
'''


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    YELLOWFILL = '\033[103m'


def load_module_from_file(filepath):
    """Initializing of all classes"""

    class_inst = None
    expected_class = filepath.split("/")[-1].split(".py")[0]

    mod_name, file_ext = os.path.splitext(os.path.split(filepath)[-1])

    if file_ext.lower() == '.py':
        py_mod = imp.load_source(mod_name, filepath)

    elif file_ext.lower() == '.pyc':
        py_mod = imp.load_compiled(mod_name, filepath)

    if hasattr(py_mod, expected_class):
        class_inst = getattr(py_mod, expected_class)()
    else:
        return bcolors().FAIL + expected_class + " not found in " + filepath + bcolors().ENDC

    return class_inst


def load_plugins(path):
    """Importing all plugins from Plugins folder.
    Returns list of initialized plugins. Can be provided to Processor"""

    sys.path.append(path)
    list_of_instances = list()
    for file_name in os.listdir(path):
        if file_name == "__init__.py":
            pass
        elif file_name.endswith(".py"):
            print bcolors().YELLOWFILL + "IMPORTING Plugin: " + bcolors().ENDC + file_name.split(".")[0]
            __import__(file_name.split(".py")[0])
            list_of_instances.append(load_module_from_file(path + "/" + file_name))
        else:
            pass
    return list_of_instances


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


# class Listener(object):
#     def getText(self):
#         r = sr.Recognizer()
#         with sr.Microphone() as source:
#             r.adjust_for_ambient_noise(source)
#             try:
#                 audio = r.listen(source)
#                 recognize = r.recognize_google(audio)
#                 recognize_lower = recognize.lower()
#                 return str(recognize_lower)
#             except Exception:
#                 pass


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


# class ConsoleInput(object):
#     def getText(self):
#         inp = raw_input("Enter text: ")
#         return inp


class Inputs(object):
    def load_input_from_file(self, filepath):
        input_inst = None
        expected_class = filepath.split("/")[-1].split(".py")[0]

        mod_name, file_ext = os.path.splitext(os.path.split(filepath)[-1])

        if file_ext.lower() == '.py':
            py_mod = imp.load_source(mod_name, filepath)

        elif file_ext.lower() == '.pyc':
            py_mod = imp.load_compiled(mod_name, filepath)

        if hasattr(py_mod, expected_class):
            input_inst = getattr(py_mod, expected_class)()
        else:
            return bcolors().FAIL + expected_class + " not found in " + filepath + bcolors().ENDC

        return input_inst

    # def load_inputs(self,path=inputs_directory):
    #     sys.path.append(path)
    #     list_of_inputs = list()
    #     for file_name in os.listdir(path):
    #         if file_name == "__init__.py":
    #             pass
    #         elif file_name.endswith(".py"):
    #             print bcolors().YELLOWFILL + "IMPORTING input:" + bcolors().ENDC + file_name.split(".")[0]
    #             __import__(file_name.split(".py")[0])
    #             list_of_inputs.append(self.load_input_from_file(path + "/" + file_name))
    #         else:
    #             pass
    #     return list_of_inputs

    def getInputList(self, path=inputs_directory):
        sys.path.append(path)
        inputs_dict = dict()
        for file in os.listdir(path):
            if file == "__init__.py":
                pass
            elif file.endswith(".py"):
                inputs_dict[file.split(".py")[0]] = self.load_input_from_file(path + "/" + file)
            else:
                pass
        for input_name, object in inputs_dict.iteritems():
            yield input_name


# class ChooseInput(object):
#     def __init__(self):
#         inputs = Inputs()
#         self.load_inputs = inputs.getInputList()
#
#     def returnInput(self):
#         for inp in self.load_inputs:
#             print inp




# processor = Processor(load_plugins(plugins_directory))
# assistant = Assistant(processor, ConsoleInput())
# assistant.start()
for i in Inputs().getInputList():
    print i

x = raw_input("Enter input to use: ")
Inputs().load_input_from_file(inputs_directory + "/" + x + ".py")
print sys.modules.keys()