import platform

import wx


class Frame(wx.Frame):
    def __init__(self, title="Speach recognize for os " + platform.system()):
        wx.Frame.__init__(self, parent=None, title=title)
        self.Bind(wx.EVT_CLOSE, self.onClose)

        panel = wx.Panel(self)
        box = wx.GridSizer(wx.HORIZONTAL)

        self.control = wx.StaticText(panel, label="Hey, talk to me", size=(100, 100))

        close = wx.Button(panel, wx.ID_CLOSE, "Close")
        close.Bind(wx.EVT_BUTTON, self.onClose)

        self.check_box = wx.CheckBox(panel, label="mute")
        self.check_box.Bind(wx.EVT_CHECKBOX, self.OnPress, self.check_box)

        box.Add(self.control, 0, wx.ALL, 10)
        box.Add(self.check_box, 1, wx.ALL, 10)
        box.Add(close, 2, wx.ALL, 10)

        panel.SetSizer(box)
        panel.Show()

    def OnPress(self, event):
        if self.check_box.IsChecked():
            self.control.SetLabel("I'm not listening to you")
            self.control.SetSize((100, 100))
        else:
            self.control.SetLabel("Hey, talk to me")

    def onClose(self, event):
        dialog = wx.MessageDialog(self, "Do you really want to close this application?", "Confirm Exit",
                                  wx.OK | wx.CANCEL | wx.ICON_QUESTION)
        result = dialog.ShowModal()
        dialog.Destroy()
        if result == wx.ID_OK:
            self.Destroy()


app = wx.App()
frame = Frame()
frame.Show()
app.MainLoop()
