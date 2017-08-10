import os
import webbrowser

cur_dir = os.path.dirname(os.path.abspath(__file__))
file_path = cur_dir + "/wsl.bin"


class SiteOpenExecutor(object):
    def getValuesFromFile(self, file=file_path):
        with open(file, "r") as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        d = dict()
        for i in content:
            d[i.split("=")[0]] = i.split("=")[1]
        return d

    def putValuesToFile(self, file=file_path):
        valuedict = self.getValuesFromFile()
        with open(file, "a+") as f:
            for key, value in valuedict.items():
                if value.startswith("http://") or value.startswith("https://"):
                    line = key + "=" + value + "\n"
                else:
                    line = key + "=" + "http://" + value + "\n"
                f.write(line)
            return f.close()

    def addWebSite(self, text, inp):
        site = inp.getText("Please, enter web page URL: ")
        web_dict = dict()
        web_dict[text] = site
        return web_dict

    def execute(self, text):
        url_dictionary = self.getValuesFromFile()
        for key, value in url_dictionary.items():
            if key in text:
                return webbrowser.open_new(value)
        return

    def procentCount(self, text):
        valuedict = self.getValuesFromFile()
        keywords = ["web site", "site", " open site", "open"]
        for word in keywords:
            if word in text:
                for i in text.split(" "):
                    if i in valuedict.iterkeys():
                        return 1
        return 0

    def nothingCanDo(self):
        pass