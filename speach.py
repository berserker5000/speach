import platform
import re
import time
import webbrowser

import pyttsx
import speech_recognition as sr


_os = platform.system()
if _os == "Linux":
    from linux_commands import *
elif _os == "Windows":
    from windows_commands import *


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


def comparator(lst, text):  # lst = set, text = string
    t1 = text.split(" ")  # t1 = list
    for word in t1:
        if word in lst:
            return word
    return ""


def google_search(text):
    split_text = text.split(" ")
    google = "http://google.com#q="
    search_string = google + "+".join(split_text)
    return webbrowser.open_new(search_string)


def what_to_do(recognize):
    speaking("Sorry, I don't know how to proceed with " + recognize)
    speaking("Let's search your question with google!")
    return google_search(recognize)


def mainfunction(source):
    audio = r.listen(source)
    recognize = r.recognize_google(audio)
    recognize_lower = recognize.lower()
    if "mute" in recognize_lower.split(" "):
        mute_system()
    elif "unmute" in recognize_lower.split(" "):
        unmute_system()
    elif "calculator" in recognize_lower.split(" "):
        run_calculator()
    elif recognize_lower == "open google":
        webbrowser.open_new("http://google.com")
    elif recognize_lower.startswith("search for"):
        encode = "".join(recognize.encode("ascii", "ignore"))
        google_search(encode.partition("search for")[2])
    elif recognize_lower == "exit":
        exit()
    elif "set volume" in recognize_lower:
        vol_encode = "".join(recognize.encode("ascii", "ignore"))
        adjust_volume(re.findall('(\d)', vol_encode))
    elif "time" in recognize_lower:
        speaking(current_time())
    else:
        comp = comparator(generate_sw_list(), recognize_lower)
        if comp != "":
            speaking("Trying to run " + str(comp))
            try:
                run_bash_command(comp)
            except:
                what_to_do(recognize)
        else:
            what_to_do(recognize)


if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2)
        speaking("Hello master. I'm Listening to you.")
        while 1:
            try:
                mainfunction(source)
            except sr.UnknownValueError:
                pass
