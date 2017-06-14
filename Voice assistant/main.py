import os
import platform

import pyttsx
import re
import subprocess
import time
import webbrowser
import speech_recognition as sr


class Windows_commands(object):
    def generate_sw_list(self):
        main_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
        directory = os.walk(main_path)
        names = dict()
        for root, dirs, files in directory:
            for f in files:
                if f.endswith("lnk"):
                    names[f.split(".lnk")[0].lower()] = ('"' + root + "\\" + f + '"')
        return names

    def mute_system(self):
        return os.popen2("nircmd.exe mutesysvolume 1")

    def unmute_system(self):
        return os.popen2("nircmd.exe mutesysvolume 0")

    def run_calculator(self):
        return os.popen2("calc")

    def adjust_volume(self, number):
        if type(number) == list:
            number = "".join(number)
            num = (int(number) * 65535) / 100
            return os.popen2("nircmd.exe setsysvolume " + str(num))

    def run_bash_command(self, command):
        return os.popen2(command)


class Linux_commands(object):
    def generate_sw_list(self):
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

        return w

    def run_bash_command(self, command):
        process = subprocess.check_output(['bash', '-c', command])
        return process

    def mute_system(self):
        return os.popen2("amixer -D pulse sset Master mute")

    def unmute_system(self):
        return os.popen2("amixer -D pulse sset Master unmute")

    def run_calculator(self):
        return os.popen2("gnome-calculator")

    def adjust_volume(self, number):
        if type(number) == list:
            number = "".join(number)
            return os.popen2("amixer -D pulse sset Master " + str(number) + "%")


class General_commands(object):

    def __init__(self, recognizer):
        self.recognizer = recognizer

    def current_time(self):
        return time.strftime("%A %d of %b %Y year %H hours %M minutes")

    def comparator(self, lst, text):
        t1 = text.split(" ")
        if type(lst) is dict:
            output = dict()
            lnk = list()
            for key, value in lst.iteritems():
                for word in t1:
                    if word.lower() in key.split(" "):
                        output[value] = word.lower()

            for key, value in output.iteritems():
                if value in t1:
                    lnk.append(key)
            return lnk

        else:
            for word in t1:
                if word in lst:
                    return word
        return ""

    def google_search(self, text):
        split_text = text.split(" ")
        google = "http://google.com#q="
        search_string = google + "+".join(split_text)
        return webbrowser.open_new(search_string)

    def what_to_do(self, recognize):
        self.recognizer("Sorry, I don't know how to proceed with " + recognize)
        self.recognizer("Let's search your question with google!")
        return self.google_search(recognize)

class Speaking():

    def __init__(self):
        self.engine = pyttsx.init()

    def speak(self,text):
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)
        self.engine.setProperty('voice', 'english')
        self.engine.setProperty('rate', 150)
        self.engine.say(text)
        return self.engine.runAndWait()


class Speach_recognize(object):

    def __init__(self):
        self.r = sr.Recognizer()
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source)


            # while 1:
            #     try:
            #         .mainfunction(source)
            #     except sr.UnknownValueError:
            #         pass
            # else:
            #     pass

class OS_info(object):

    def get_os_type(self):
        return platform.system()



class Decission_maker(object):


    def __init__(self, commands):
        self.commands = commands
        self.recognizer = Speach_recognize()
        self.genereal_commands = General_commands(self.recognizer)


    # def decision(self, source):
    #     audio = self.recognizer.r.listen(source)
    #     recognize = self.recognizer.r.recognize_google(audio)
    #     recognize_lower = recognize.lower()
    #     if "mute" in recognize_lower.split(" "):
    #         self.system.mute_system()
    #     elif "unmute" in recognize_lower.split(" "):
    #         self.system.unmute_system()
    #     elif "calculator" in recognize_lower.split(" "):
    #         self.system.run_calculator()
    #     elif recognize_lower == "open google":
    #         webbrowser.open_new("http://google.com")
    #     elif recognize_lower.startswith("search for"):
    #         encode = "".join(recognize.encode("ascii", "ignore"))
    #         General_commands.google_search(encode.partition("search for")[2])
    #     elif recognize_lower == "exit":
    #         exit()
    #     elif "set volume" in recognize_lower:
    #         vol_encode = "".join(recognize.encode("ascii", "ignore"))
    #         self.system.adjust_volume(re.findall('(\d)', vol_encode))
    #     elif "time" in recognize_lower:
    #         General_commands.speaking(self,self.current_time())
    #     else:
    #         comp = General_commands.comparator(self,self.system.generate_sw_list(), recognize_lower)
    #         if comp != "" and self.__os == "Linux":
    #             General_commands.speaking(self,"Trying to run " + str(comp))
    #             try:
    #                 self.system.run_bash_command(comp)
    #             except Exception:
    #                 General_commands.speaking(self,"I had an exception. Can't proceed with your request.")
    #         elif comp != "" and self.__os == "Windows":
    #             if len(comp) > 1:
    #                 dictionary = dict()
    #                 i = 0
    #                 General_commands.speaking(self,"I have found several programs. Please choose one to run")
    #                 for c in comp:
    #                     i += 1
    #                     print(str(i) + ":" + c.split("\\")[-1].split(".lnk")[0])
    #                     dictionary[i] = c
    #                 inp = input("Enter number: ")
    #                 for key, value in dictionary.iteritems():
    #                     if inp == key:
    #                         os.popen2(value)
    #
    #             else:
    #                 General_commands.speaking(self,"Trying to run " + str(comp[0].split("\\")[-1].split(".")[0]))
    #                 os.popen2(comp[0])
    #         else:
    #             General_commands.what_to_do(self,recognize)



if __name__ == '__main__':
    _os = OS_info().get_os_type()
    if _os == "Linux":
        commands = Linux_commands()
    elif _os == "Windows":
        commands = Windows_commands()
    decision = Decission_maker(commands)