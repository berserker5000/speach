import os
import platform
import subprocess
import time

import pyttsx
import speech_recognition as sr

_os = platform.system()


class GeneralProgransExecutor():
    def executor(self, text):
        pass

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
    @staticmethod
    def __softwareLinuxGenerator():
        tmp_name = '/tmp/software_list_tmp.txt'
        q, e = [], []
        w = dict()

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
            w[i[0]] = i[0]
        q, e = None, None
        return w

    @staticmethod
    def __softwareWindowsGenerator():
        main_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
        directory = os.walk(main_path)
        names = dict()
        for root, dirs, files in directory:
            for f in files:
                if f.endswith("lnk"):
                    names[f.split(".lnk")[0].lower()] = ('"' + root + "\\" + f + '"')
        return names

    def execute(self, text):  # processing text
        splited_text = text.split(" ")
        if _os == "Linux":
            software_list = self.__softwareLinuxGenerator()
        elif _os == "Windows":
            software_list = self.__softwareWindowsGenerator()

        return software_list  # os.popen2(program)

    def key_words(self):
        pass

    def percentCount(self):
        pass


class WebSearchExecutor():
    def execute(self, text):
        pass

    def key_words(self):
        pass

    def percentCount(self):
        pass


class SiteOpenExecutor():
    def execute(self, text):
        pass

    def key_words(self):
        pass

    def percentCount(self):
        pass


