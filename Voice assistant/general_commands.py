import os
import time
import webbrowser

import pyttsx


def current_time():
    return time.strftime("%A %d of %b %Y year %H hours %M minutes")


def speaking(text):
    engine = pyttsx.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('voice', 'english')
    engine.setProperty('rate', 150)
    engine.say(text)
    return engine.runAndWait()


def comparator(lst, text):
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


def google_search(text):
    split_text = text.split(" ")
    google = "http://google.com#q="
    search_string = google + "+".join(split_text)
    return webbrowser.open_new(search_string)


def what_to_do(recognize):
    speaking("Sorry, I don't know how to proceed with " + recognize)
    speaking("Let's search your question with google!")
    return google_search(recognize)
