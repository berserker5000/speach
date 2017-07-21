import webbrowser


class WebSite():
    def getValuesFromFile(self, file="wsl.bin"):
        with open(file, "r") as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        d = dict()
        for i in content:
            d[i.split("=")[0]] = i.split("=")[1]
        return d

    def putValuesToFile(self, file="wsl.bin"):
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


web = WebSite()
web.execute("I want site google to be opened")