import os
import platform
import webbrowser

import speech_recognition as sr


def get_os_type():
        return platform.system()


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


def run_calculator(_os):
    if _os == "Linux":
        return os.popen2("gnome-calculator")
    elif _os == "Windows":
        return os.popen2("calc")

def google_search(text):
    split_text = text.split(" ")
    google = "http://google.com#q="
    search_string = google + "+".join(split_text)
    return webbrowser.open_new(search_string)


def mainfunction(source):
    _os = get_os_type()
    audio = r.listen(source)
    recognize = r.recognize_google(audio)
    recognize_lower = recognize.lower()
    print(recognize)
    if "mute" in recognize_lower.split(" "):
        mute_system(_os)
    elif "unmute" in recognize_lower.split(" "):
        unmute_system(_os)
    elif "calc" or "calculator" in recognize_lower.split(" "):
        run_calculator(_os)
    elif recognize_lower == "open google":
        webbrowser.open_new("http://google.com")
    elif recognize_lower.startswith("search for"):
        encode = "".join(recognize.encode("ascii", "ignore"))
        google_search(encode.partition("search for")[2])
    elif recognize_lower == "exit":
        exit()
    else:
        print "This is string you told: " + recognize


if __name__ == "__main__":
    r = sr.Recognizer()
    print("I'm listening to you!")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        while 1:
            try:
                mainfunction(source)
            except sr.UnknownValueError:
                pass