import speech_recognition as sr


class VoiceInput(object):
    def getText(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            try:
                audio = r.listen(source)
                recognize = r.recognize_google(audio)
                recognize_lower = recognize.lower()
                if recognize_lower == None:
                    pass
                return str(recognize_lower)
            except Exception:
                pass