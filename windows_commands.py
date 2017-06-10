__author__ = 'Administrator'
import os


def mute_system():
    return os.popen2("nircmd.exe mutesysvolume 1")


def unmute_system():
    return os.popen2("nircmd.exe mutesysvolume 0")


def run_calculator():
    return os.popen2("calc")


def adjust_volume(number):
    if type(number) == list:
        number = "".join(number)
        num = (int(number) * 65535) / 100
        return os.popen2("nircmd.exe setsysvolume " + str(num))


def run_bash_command(command):
    com = command.split(" ")
    main_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
    directory = os.walk(main_path)
    names, output = dict(), dict()
    for root, dirs, files in directory:
        for f in files:
            if f.endswith("lnk"):
                names[f.split(".lnk")[0].lower()] = ('"' + root + f + '"')

    for key, value in names.iteritems():
        for word in com:
            if word.lower() in key:
                output[value] = word.lower()

    for key, value in output.iteritems():
        print("For " + value + ". I found next programs: " + key)


run_bash_command("run fucking Anaconda viber pytty python")
os.popen2("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Python 2.7IDLE (Python GUI).lnk")
