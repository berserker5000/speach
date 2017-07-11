
import pyttsx
import speech_recognition as sr

class Speaker():
    def __init__(self, language="english"):
        self.engine = pyttsx.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)
        self.engine.setProperty('voice', language)
        self.engine.setProperty('rate', 150)

    def speak(self, text):
        self.engine.say(text)
        return self.engine.runAndWait()


class Listener():
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


class Processor():
    def __init__(self, *commands):
        self.commands = commands

    def execute(self, text):
        identifier = 0
        for i in self.commands:
            if i.procent(text) == 1:
                identifier = i.execute(text)
                return identifier
            else:
                pass
        return identifier
