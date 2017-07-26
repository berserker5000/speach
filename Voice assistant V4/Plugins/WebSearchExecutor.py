import webbrowser

class WebSearchExecutor():
    keys = ["search", "look for", "search in internet for", "look in internet for", "find in internet", "find for",
            "search for"]
    def execute(self, text):
        for key in self.keys:
            if key in text:
                return webbrowser.open_new("https://google.com/#q=" + " ".join(text.split(key)[1].split(" ")[1:]))
            else:
                pass
        return

    def procentCount(self, text):
        for key in self.keys:
            if key in text:
                return 1
        return 0

    def nothingCanDo(self):
        pass