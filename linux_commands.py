import subprocess


def linux_soft_list():
    return subprocess.check_call(["apt", "list", "--installed"], stdout=open('/tmp/software_list_tmp.txt', 'wb'),
                                 stderr=subprocess.STDOUT)


def generate_sw_list():
    test = ["docker", 'zoom']
    tmp_name = '/tmp/software_list_tmp.txt'
    q, w, e = [], [], []

    try:
        linux_soft_list()
    except Exception:
        return "can't proceed with temp software list"

    with open(tmp_name, 'r') as f:
        for line in f:
            q.append(line)
        f.close()

    for i in q:
        e.append(i.split('/'))

    for i in e:
        w.append(i[0])

    for i in test:
        for o in w[4:]:
            if i in o:
                print o



def run_bash_command(command):
    process = subprocess.check_output(['bash', '-c',command])
    return process

