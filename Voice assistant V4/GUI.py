import platform
import wx
import wx.animate


class Frame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Frame, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fitem = fileMenu.Append(wx.ID_EXIT, "Quit", "Quit application")
        menubar.Append(fileMenu, "&File")
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_CLOSE, self.onClose)
        self.Bind(wx.EVT_MENU, self.onClose, fitem)

        self.SetSize((300, 200))
        self.SetTitle("Voice assistand for " + platform.system())
        self.Centre()
        self.Show(True)

    #     gif_file_name = "1.gif"
    #     panel = wx.Panel(self)
    #     box = wx.GridSizer(wx.HORIZONTAL)
    #
    #     self.control = wx.TextCtrl(panel, size=(100, 100))
    #
    #     close = wx.Button(panel, wx.ID_CLOSE, "Close")
    #     close.Bind(wx.EVT_BUTTON, self.onClose)
    #
    #     self.check_box = wx.CheckBox(panel, label="mute")
    #     self.check_box.Bind(wx.EVT_CHECKBOX, self.OnPress, self.check_box)
    #
    #     self.gif = wx.animate.GIFAnimationCtrl(self, id=-1, filename=gif_file_name, pos=(wx.Width, wx.Height))
    #
    #     self.gif.Play()
    #     box.Add(self.control, 0, wx.ALL, 10)
    #     box.Add(self.check_box, 1, wx.ALL, 10)
    #     box.Add(close, 2, wx.ALL, 10)
    #
    #     panel.SetSizer(box)
    #     panel.Show()
    #
    # def OnPress(self, event):
    #     if self.check_box.IsChecked():
    #         self.control.SetValue("I'm not listening to you")
    #     else:
    #         pass
    #
    def onClose(self, event):
        dialog = wx.MessageDialog(self, "Do you really want to close this application?", "Confirm Exit",
                                  wx.OK | wx.CANCEL | wx.ICON_QUESTION)
        result = dialog.ShowModal()
        dialog.Destroy()
        if result == wx.ID_OK:
            self.Destroy()


def main_gui():
    ex = wx.App()
    Frame(None)
    ex.MainLoop()


if __name__ == '__main__':
    main_gui()