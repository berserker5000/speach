import os,time,re
import platform
import webbrowser
import pyttsx
import speech_recognition as sr


def get_os_type():
    return platform.system()

def current_time():
    return time.strftime("%A %d of %b %Y year %H hours %M minutes")

def speaking(text):
    engine = pyttsx.init()
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

def adjust_volume(_os, number):
    if type(number) == list:
        number = "".join(number)
    if _os == "Linux":
        return os.popen2("amixer -D pulse sset Master " + str(number) + "%")
    elif _os == "Windows":
        num = (int(number) * 65535) / 100
        return os.popen2("nircmd.exe setsysvolume " + str(num))


def mainfunction(source):
    _os = get_os_type()
    audio = r.listen(source)
    recognize = r.recognize_google(audio)
    recognize_lower = recognize.lower()
    #print(recognize)
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
        adjust_volume(_os,re.findall('(\d)',vol_encode))
    elif "time" in recognize_lower:
        speaking(current_time())
    else:
        print(recognize)
        speaking("Sorry, I don't know how to proceed with " + recognize)


if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone(
    ) as source:
        r.adjust_for_ambient_noise(source,duration=2)
        speaking("Hello master. I'm Listening to you.")
        while 1:
            try:
                mainfunction(source)
            except sr.UnknownValueError:
                pass
