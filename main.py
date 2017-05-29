import windows_commands
import speech_recognition as sr
import platform


class Main(object):

    def recognizer(self):
        self.r = sr.Recognizer()
        print("I'm listening to you!")
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source)
            while 1:
                try:
                    self.mainfunction(source)
                except sr.UnknownValueError:
                    pass

    def get_os_type(self):
        return platform.system()

    def mainfunction(self,source):
        audio = self.r.listen(source)
        recognize = self.r.recognize_google(audio)
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
            encode = "".join(recognize.encode("ascii", "ignore"))
            google_search(encode.partition("search for")[2])
        elif recognize_lower == "exit":
            exit()
        else:
            print "This is string you told: " + recognize