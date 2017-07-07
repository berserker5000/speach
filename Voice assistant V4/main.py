import os
import platform
import subprocess
import time

import pyttsx
import speech_recognition as sr

_os = platform.system()


class SoftwareListGenerator():
    def Linux(self):
        tmp_name = '/tmp/software_list_tmp.txt'
        q, e = [], []
        w = set()

        try:
            subprocess.check_call(["apt", "list", "--installed"], stdout=open('/tmp/software_list_tmp.txt', 'wb'),
                                  stderr=subprocess.STDOUT)
        except Exception:
            return "can't proceed with temp software list"

        with open(tmp_name, 'r') as f:
            for line in f:
                q.append(line)
            f.close()

        for i in q:
            e.append(i.split('/'))

        for i in e:
            w.add(i[0])
        q, e = None, None
        return w

    def Windows(self):
        main_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
        directory = os.walk(main_path)
        names = dict()
        for root, dirs, files in directory:
            for f in files:
                if f.endswith("lnk"):
                    names[f.split(".lnk")[0].lower()] = ('"' + root + "\\" + f + '"')
        return names


class ExecuteProgram():
    def execute(self, program):
        return os.popen2(program)


class Time():
    def get_current_time(self):
        return time.strftime("%A %d of %b %Y year %H hours %M minutes")


class Speaker():
    def __init__(self, language="english"):
        self.engine = pyttsx.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)
        self.engine.setProperty('voice', language)
        self.engine.setProperty('rate', 150)

    def speak(self, text):
        self.engine.say(text)
        return self.engine.runAndWait()


class Listener():
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


class RunProgramExecutor():
    def __init__(self):
        pass

    def execute(self):
        pass

    def key_words(self):
        pass

    def percentCount(self):
        pass


class WebSearchExecutor():
    def __init__(self):
        pass

    def execute(self):
        pass

    def key_words(self):
        pass

    def percentCount(self):
        pass


class SiteOpenExecutor():
    def __init__(self):
        pass

    def execute(self):
        pass

    def key_words(self):
        pass

    def percentCount(self):
        pass


class File():
    pass


class Internet():
    pass


class Main():
    pass


class Visual():
    pass


class MultiThreading():
    pass
