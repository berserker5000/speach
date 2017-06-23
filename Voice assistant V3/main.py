import os
import platform
import re
import sqlite3
import subprocess
import time
import webbrowser

import pyttsx
import speech_recognition as sr

_os = platform.system()


class SynonimList(object):
    def open(self):
        op = ["open", "run", "start", "do"]
        return op

    def close(self):
        cl = ["close", "exit from", "exit", "leave"]
        return cl

    def remove(self):
        rm = ["remove", "delete", "wipe", "clean"]
        return rm


class DataBase(object):
    def __init__(self):
        self.conn = sqlite3.connect(database="database.db", timeout=30)
        self.c = self.conn.cursor()

    def get_commands(self, text, OperationSystem):
        self.t = text.split(" ")
        for word in self.t:
            for value in self.c.execute("SELECT Command FROM General WHERE Text=" + "'" + str(
                    word) + "'" + "and OS='" + str(OperationSystem) + "'"):
                if value[0] != None:
                    return (value[0])
                else:
                    return False

    def add_commands(self, text, OperationSystem):
        text_low = str(text).lower()
        command = raw_input("Please, enter command what to do: \n")
        self.c.execute(
            "insert into General(Command, OS,Text) values ('" + command + "\',\'" + OperationSystem + "\',\'" + text_low + "')")
        return self.conn.commit()

    def list_commands(self, OperationSystem):
        self.list_command = {}
        for value in self.c.execute("Select text, Command FROM General WHERE OS='" + OperationSystem + "'"):
            if value[0] != None:
                self.list_command[str(value[0])] = str(value[1])
        return self.list_command

    def indexed_commands(self):
        indexed_commands = {}
        i = 0
        for value in self.list_command.keys():
            i += 1
            indexed_commands[i] = value
        return indexed_commands

    def remove_command(self, os, text):
        text_low = str(text).lower()
        self.conn.cursor()
        self.c.execute("delete FROM General WHERE OS='" + str(os) + "' AND Text='" + text_low + "'")
        return self.conn.commit()


class WindowsCommands(object):
    def generate_sw_list(self):
        main_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
        directory = os.walk(main_path)
        names = dict()
        for root, dirs, files in directory:
            for f in files:
                if f.endswith("lnk"):
                    names[f.split(".lnk")[0].lower()] = ('"' + root + "\\" + f + '"')
        return names

    # def mute_system(self):
    #     return os.popen2("nircmd.exe mutesysvolume 1")
    #
    # def unmute_system(self):
    #     return os.popen2("nircmd.exe mutesysvolume 0")
    #
    # def run_calculator(self):
    #     return os.popen2("calc")

    def adjust_volume(self, number):
        if type(number) == list:
            number = "".join(number)
            num = (int(number) * 65535) / 100
            return os.popen2("nircmd.exe setsysvolume " + str(num))

            # def run_bash_command(self, command):
            #     return os.popen2(command)


class RunProgram(object):
    def __init__(self, command):
        os.popen2(str(command))


class LinuxCommands(object):
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
        q, e = None, None
        return w

    # def run_bash_command(self, command):
    #     return subprocess.check_output(['bash', '-c', command])

    # def mute_system(self):
    #     return os.popen2("amixer -D pulse sset Master mute")

    # def unmute_system(self):
    #     return os.popen2("amixer -D pulse sset Master unmute")

    # def run_calculator(self):
    #     return os.popen2("gnome-calculator")

    def adjust_volume(self, number):
        if type(number) == list:
            number = "".join(number)
            return os.popen2("amixer -D pulse sset Master " + str(number) + "%")


class GeneralCommands(object):
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

        # def run_command(self, command):
        #     return os.popen2(command)

        # def what_to_do(self, speaker, recognized_text):
        #     speaker("Sorry, I don't know how to proceed with " + recognized_text)
        #     speaker("Let's search your question with google!")
        #     return self.google_search(recognized_text)


class Speaking(object):
    def __init__(self):
        self.engine = pyttsx.init()

    def speak(self, text):
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)
        self.engine.setProperty('voice', 'english')
        self.engine.setProperty('rate', 150)
        self.engine.say(text)
        return self.engine.runAndWait()


class SpeechRecognize(object):
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


# class OsInfo(object):
#     def get_os_type(self):
#         return platform.system()


class DecisionMaker(object):
    def __init__(self, command):
        self.command = command

        self.general_commands = GeneralCommands()
        self.db = DataBase()
        self.text = SpeechRecognize().recognize()
        self.command = db.get_commands(self.text, _os)

    def decision(self, recognized_text, speak, general_command, os_type):
        if "mute" in recognized_text.split(" "):
            self.command.mute_system()
        elif "unmute" in recognized_text.split(" "):
            self.command.unmute_system()
        elif "calculator" in recognized_text.split(" "):
            self.command.run_calculator()
        elif recognized_text == "open google":
            webbrowser.open_new("http://google.com")
        elif recognized_text.startswith("search for"):
            encode = "".join(recognized_text.encode("ascii", "ignore"))
            general_command.google_search(encode.partition("search for")[2])
        elif recognized_text == "exit":
            exit()
        elif "set volume" in recognized_text:
            vol_encode = "".join(recognized_text.encode("ascii", "ignore"))
            self.command.adjust_volume(re.findall('(\d)', vol_encode))
        elif "time" in recognized_text:
            speak.speak(general_command.current_time())
        else:
            comp = general_command.comparator(self.command.generate_sw_list(), recognized_text)
            if len(comp) != 0 and os_type == "Linux":
                speak.speak("Trying to run " + str(comp))
                try:
                    self.command.run_bash_command(comp)
                except Exception:
                    speak.speak("I had an exception. Can't proceed with your request.")
            elif len(comp) != 0 and os_type == "Windows":
                if len(comp) > 1:
                    dictionary = dict()
                    i = 0
                    speak.speak("I have found several programs. Please choose one to run")
                    for c in comp:
                        i += 1
                        print(str(i) + ":" + c.split("\\")[-1].split(".lnk")[0])
                        dictionary[i] = c
                    try:
                        inp = input("Enter number: ")
                    except Exception:
                        print ("Please, enter a valid number.")
                        inp = input("Enter number: ")
                    for key, value in dictionary.iteritems():
                        if inp == key:
                            os.popen2(value)

                else:
                    speak.speak("Trying to run " + str(comp[0].split("\\")[-1].split(".")[0]))
                    os.popen2(comp[0])
            else:
                speak.speak("I didn't found anything suitable program with request " + recognized_text)
                speak.speak("Trying to find it in Google")
                general_commands.google_search(recognized_text)

    def decision2(self):
        pass


if __name__ == '__main__':
    # general_commands = GeneralCommands()
    db = DataBase()
    # db.get_commands("mute", _os)

    # db.list_commands(_os)
    # db.add_commands("copy", _os)
    # db.remove_command(os, "copy")



    # TODO: Add multithreading
    # TODO: Add face recognition
    # TODO: Make administration posibility
    # TODO: Make "access point" for administrating
