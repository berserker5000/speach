import subprocess

import speech_recognition as sr


# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source, phrase_time_limit=5)

recognize = r.recognize_google(audio)
recognize_lower=recognize.lower()

def osrun(cmd):
    PIPE = subprocess.PIPE
    p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT)


# try:
#     # for testing purposes, we're just using the default API key
#     # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
#     # instead of `r.recognize_google(audio)`
#     print("Google Speech Recognition thinks you said: " + recognize)
# except sr.UnknownValueError:
#     print("Google Speech Recognition could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Google Speech Recognition service; {0}".format(e))

if "calc" in recognize_lower:
    osrun('calc')
if recognize_lower.startswith("open"):
    print recognize
else:
    print "This is string you told: " + recognize

# def commands(command):
#     if str(command).startswith("open"):
#         open()
#     else:
#         return False
#
# def open():
#     return "This is open command"
#
# commands(recognize_lower)