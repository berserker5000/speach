import os


class WindowsProgramExecutor():
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
        s = dict()

        # generating dict with installed software
        software_dict = self.__softwareWindowsGenerator()

        # making list with elements that are suitable to request
        for element in splited_text:
            for key, value in software_dict.iteritems():
                if len(key) > 1:
                    for i in key.split(" "):
                        if element == i:
                            s[key] = value

        if len(s) == 1:
            for k, v in s.iteritems():
                return os.popen2(v)
        elif len(s) > 1:
            iterator = 0
            tmp_dict = dict()
            for k, v in s.iteritems():
                iterator += 1
                tmp_dict[iterator] = k
                print iterator, k
            try:
                choice = input("Enter number: ")
                return os.popen2(s[tmp_dict[choice]])
            except Exception:
                return

        return

    def procentCount(self, text):
        splited_text = text.split(" ")
        counter = 0

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