__author__ = 'Administrator'
import os


def generate_sw_list():
    main_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
    directory = os.walk(main_path)
    names = dict()
    for root, dirs, files in directory:
        for f in files:
            if f.endswith("lnk"):
                names[f.split(".lnk")[0].lower()] = ('"' + root + "\\" + f + '"')
    return names


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
       return os.popen2(command)