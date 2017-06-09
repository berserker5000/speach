import platform
import re

import speech_recognition as sr

from general_commands import *

_os = platform.system()
if _os == "Linux":
    from linux_commands import *
elif _os == "Windows":
    from windows_commands import *


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
                pass
        else:
            what_to_do(recognize)


if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        speaking("Hello master. I'm Listening to you.")
        while 1:
            try:
                mainfunction(source)
            except sr.UnknownValueError:
                pass
        else:
            pass
