import os
import platform
import re
import time
import webbrowser

import google
import pyttsx
import speech_recognition as sr

from linux_commands import generate_sw_list


def get_os_type():
    return platform.system()


def current_time():
    return time.strftime("%A %d of %b %Y year %H hours %M minutes")


def speaking(text):
    engine = pyttsx.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('voice', 'english')
    engine.setProperty('rate', 190)
    engine.say(text)
    return engine.runAndWait()


def mute_system(_os):
    if _os == "Linux":
        return os.popen2("amixer -D pulse sset Master 0%")
    elif _os == "Windows":
        return os.popen2("nircmd.exe mutesysvolume 1")


def unmute_system(_os):
    if _os == "Linux":
        return os.popen2("amixer -D pulse sset Master 100%")
    elif _os == "Windows":
        return os.popen2("nircmd.exe mutesysvolume 0")


def comparator(lst, text):
    t1 = text.split(" ")
    for i in lst:
        for k in t1:
            if i == k:
                return i
    return ""


def run_calculator(_os):
    if _os == "Linux":
        return os.popen2("gnome-calculator")
    elif _os == "Windows":
        return os.popen2("calc")


def unknown(text):
    x, y = [], []
    gs = google.search('https://google.com/#q=' + str(text), pause=0, stop=15)
    for link in gs:
        x.append(link)

    for i in x:
        y.append(i.split('/')[2])

    dictionary = dict(zip(x, y))
    return dictionary


def google_search(text):
    split_text = text.split(" ")
    google = "http://google.com#q="
    search_string = google + "+".join(split_text)
    return webbrowser.open_new(search_string)


def adjust_volume(_os, number):
    if type(number) == list:
        number = "".join(number)
    if _os == "Linux":
        return os.popen2("amixer -D pulse sset Master " + str(number) + "%")
    elif _os == "Windows":
        num = (int(number) * 65535) / 100
        return os.popen2("nircmd.exe setsysvolume " + str(num))


def question(audio, action):
    yes = ['yep', 'yes', 'ea', ' yeah']
    no = ['no', 'nope']
    speaking("Are you sure you want to " + str(audio))
    for i in yes:
        if i in audio:
            return speaking("As you wish. I will do " + str(audio)), action
    for i in no:
        if i in audio:
            return speaking("Ok, I wouldn't do " + str(audio))


def mainfunction(source):
    _os = get_os_type()
    audio = r.listen(source)
    recognize = r.recognize_google(audio)
    recognize_lower = recognize.lower()
    if "mute" in recognize_lower.split(" "):
        mute_system(_os)
    elif "unmute" in recognize_lower.split(" "):
        unmute_system(_os)
    elif "calculator" in recognize_lower.split(" "):
        run_calculator(_os)
    elif recognize_lower == "open google":
        webbrowser.open_new("http://google.com")
    elif recognize_lower.startswith("search for"):
        encode = "".join(recognize.encode("ascii", "ignore"))
        google_search(encode.partition("search for")[2])
    elif recognize_lower == "exit":
        exit()
    elif "set volume" in recognize_lower:
        vol_encode = "".join(recognize.encode("ascii", "ignore"))
        adjust_volume(_os, re.findall('(\d)', vol_encode))
    elif "time" in recognize_lower:
        speaking(current_time())
    elif comparator(generate_sw_list(),recognize_lower) != "":
        speaking("Trying to run " + str(comparator(generate_sw_list(),recognize_lower)))
        try:
            os.popen2(comparator(generate_sw_list(),recognize_lower))
        except:
            speaking("Sorry, I don't know how to proceed with " + recognize)
            speaking("Let's search your question with google!")
            google_search(recognize_lower)
    else:
        speaking("Sorry, I don't know how to proceed with " + recognize)
        speaking("Let's search your question with google!")
        google_search(recognize_lower)


if __name__ == "__main__":
    generate_sw_list()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2)
        speaking("Hello master. I'm Listening to you.")
        while 1:
            try:
                mainfunction(source)
            except sr.UnknownValueError:
                pass
