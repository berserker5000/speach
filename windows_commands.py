import os, webbrowser
from main import Main as mn

class Internet_commands(object):

    def google_search(self,text):
        split_text = text.split(" ")
        google = "http://google.com#q="
        search_string = google + "+".join(split_text)
        return webbrowser.open_new(search_string)




    def test(self):

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
            encode = "".join(mn.recognizer.encode("ascii", "ignore"))
            self.google_search(encode.partition("search for")[2])
        elif recognize_lower == "exit":
            exit()
        else:
            print "This is string you told: " + recognize