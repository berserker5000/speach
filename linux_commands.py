import os
import subprocess


def generate_sw_list():
    tmp_name = '/tmp/software_list_tmp.txt'
    q, e = [], []
    w = set()

    try:
        subprocess.check_call(["apt", "list", "--installed"], stdout=open('/tmp/software_list_tmp.txt', 'wb'),
                              stderr=subprocess.STDOUT)
    except Exception:
        return "can't proceed with temp software list"

    with open(tmp_name, 'r') as f:
        for line in f:
            q.append(line)
        f.close()

    for i in q:
        e.append(i.split('/'))

    for i in e:
        w.add(i[0])

    return w


def run_bash_command(command):
    process = subprocess.check_output(['bash', '-c', command])
    return process


def mute_system():
    return os.popen2("amixer -D pulse sset Master 0%")


def unmute_system():
    return os.popen2("amixer -D pulse sset Master 100%")


def run_calculator():
    return os.popen2("gnome-calculator")


def adjust_volume(number):
    if type(number) == list:
        number = "".join(number)
        return os.popen2("amixer -D pulse sset Master " + str(number) + "%")
