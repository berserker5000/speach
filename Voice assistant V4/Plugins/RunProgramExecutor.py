import os
import platform

import subprocess

_os = platform.system()


class RunProgramExecutor():
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

    @staticmethod
    def __softwareWindowsGenerator():
        main_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
        directory = os.walk(main_path)
        names = dict()
        for root, dirs, files in directory:
            for f in files:
                if f.endswith("lnk"):
                    names[f.split(".lnk")[0].lower()] = ('"' + root + "\\" + f + '"')
        return names

    def execute(self, text):  # processing text
        splited_text = text.split(" ")
        s = set()
        if _os == "Linux":
            software_dict = self.__softwareLinuxGenerator()
        elif _os == "Windows":
            software_dict = self.__softwareWindowsGenerator()
        for element in splited_text:
            get_command = " ".join(text.split(element)[1].split(" ")[1:]).split(" ")
            for each in get_command:
                for key, value in software_dict.iteritems():
                    for i in value:
                        if each == i:
                            s.add(key)
        if len(s) == 1:
            os.popen2(software_dict[str(list(s)[0])][0])
        elif len(s) == 0:
            return
        else:
            iterator = 0
            d = dict()
            for i in s:
                iterator += 1
                d[iterator] = i
            for i, v in d.iteritems():
                print i, v
            inp = input("Enter numberwhat to run: ")
            os.popen2(software_dict[d[inp]][0])
        return



    def procentCount(self, text):
        splited_text = text.split(" ")
        counter = 0

        if _os == "Linux":
            software_dict = self.__softwareLinuxGenerator()
        elif _os == "Windows":
            software_dict = self.__softwareWindowsGenerator()

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

