from tkinter import *


class App:
    def __init__(self):
        self.root = Tk()
        self.hidden = False

        self.var = IntVar()
        self.button = Button(self.root, text="Quit", fg="red", command=quit, width=15, highlightbackground="red").grid(
            row=0, column=1)
        self.e = Entry(self.root)
        self.e.grid(row=1, column=0)
        Checkbutton(self.root, text='Listen to me', command=self.toggle_entry).grid(row=0, column=0)

    def toggle_entry(self):

        if self.hidden:
            self.e.grid()
        else:
            self.e.grid_remove()
        self.hidden = not self.hidden

    def start(self):
        self.root.mainloop()


App().start()