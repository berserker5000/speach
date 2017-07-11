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
        q, e = None, None
        return w

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
        listed = set()
        iterator = 0
        if _os == "Linux":
            software_list = self.__softwareLinuxGenerator()
        elif _os == "Windows":
            software_list = self.__softwareWindowsGenerator()
        for element in splited_text:
            if element in self.key_words():
                get_command = text.split(element)[1]
                for key, value in software_list.iteritems():
                    if get_command in key:
                        return os.popen2(value)
                    else:
                        for command_word in get_command.split():
                            if command_word in key:
                                listed.add(value)
                                if len(listed) > 1:
                                    print("Found more then 1 item, please choose")
                                    for i in listed:
                                        iterator += 1
                                        print(iterator, ":", i)
                                else:
                                    return os.popen2(list(listed)[0])
            else:
                print "No such program"

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
