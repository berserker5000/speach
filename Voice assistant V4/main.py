import os
import sys

import pyttsx
import speech_recognition as sr

cur_dir = os.path.dirname(os.path.abspath(__file__))
path_name = cur_dir + "/Plugins"

import imp


def load_from_file(filepath):
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
        return expected_class + " not found in " + filepath

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
            print "IMPORTING: " + file_name.split(".")[0]
            __import__(file_name.split(".py")[0])
            list_of_instances.append(load_from_file(path + "/" + file_name))
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


class Listener(object):
    def recognize(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            try:
                audio = r.listen(source)
                recognize = r.recognize_google(audio)
                recognize_lower = recognize.lower()
                return str(recognize_lower)
            except sr.UnknownValueError:
                pass


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


class ConsoleInput(object):
    def getText(self):
        inp = raw_input("Enter text: ")
        return inp


class Main(object):
    pass


processor = Processor(load_plugins(path_name))
assistant = Assistant(processor, ConsoleInput())
assistant.start()
