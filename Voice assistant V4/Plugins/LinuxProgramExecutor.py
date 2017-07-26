import os

import subprocess


class LinuxProgramExecutor():
    @staticmethod
    def __softwareLinuxGenerator():
        tmp_name = '/tmp/software_list_tmp.txt'
        q, e = [], []
        w = dict()

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
            w[i[0]] = i[0]
        q, e = dict(), None
        for key, value in w.iteritems():
            new_key_linux = key.split("-")
            q[value] = new_key_linux
        return q

    def execute(self, text):  # processing text
        splited_text = text.split(" ")
        s = set()

        # defining OS and generating dict with installed software
        software_dict = self.__softwareLinuxGenerator()

        # making list with elements that are suitable to request
        for element in splited_text:
            get_command = " ".join(text.split(element)[1].split(" ")[1:]).split(" ")
            for each in get_command:
                for key, value in software_dict.iteritems():
                    for i in value:
                        if each == i:
                            s.add(key)

        # runing suitable program
        if len(s) == 1:
            os.popen2(software_dict[str(list(s)[0])][0])
        elif len(s) == 0:
            return "No program was found"
        else:
            iterator = 0
            d = dict()
            for i in s:
                iterator += 1
                d[iterator] = i
            for i, v in d.iteritems():
                print i, v
            inp = input("Enter number what to run: ")
            os.popen2(software_dict[d[inp]][0])
        return "Can't run any program from your list"

    def procentCount(self, text):
        splited_text = text.split(" ")
        counter = 0

        software_dict = self.__softwareLinuxGenerator()

        for word in splited_text:
            for key, value in software_dict.iteritems():
                if word == key:
                    counter = 1
                elif len(key.split(" ")) > 1:
                    for i in key.split(" "):
                        if word == i:
                            counter = 1
                else:
                    pass
        return counter

    def nothingCanDo(self):
        pass