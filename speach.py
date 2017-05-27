import subprocess
import webbrowser
import os
import speech_recognition as sr


def google_search(text):
    split_text = text.split(" ")
    google = "http://google.com#q="
    search_string = google + "+".join(split_text)
    return webbrowser.open_new(search_string)

def mainfunction(source):
    audio = r.listen(source)
    recognize = r.recognize_google(audio)
    recognize_lower = recognize.lower()
    print(recognize)
    if recognize_lower == "mute":
        os.popen2("nircmd.exe mutesysvolume 1")
    elif recognize_lower == "unmute":
        os.popen2("nircmd.exe mutesysvolume 0")
    elif "calc" in recognize_lower:
        os.popen2("calc")
    elif recognize_lower.startswith("run"):
        print recognize
    elif recognize_lower == "open google":
        webbrowser.open_new("http://google.com")
    elif recognize_lower.startswith("search for"):
       # print(type(recognize))
        encode = "".join(recognize.encode("ascii", "ignore"))
       # print(type(encode.split(" ")[2:]))
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