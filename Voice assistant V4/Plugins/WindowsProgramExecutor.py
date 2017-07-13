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
        s = set()

        # defining OS and generating dict with installed software
        software_dict = self.__softwareWindowsGenerator()

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