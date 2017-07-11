import platform
import wx
import wx.animate


class Frame(wx.Frame):
    def __init__(self, title="Speach recognize for os " + platform.system()):
        wx.Frame.__init__(self, parent=None, title=title, size=(900, 900))
        self.Bind(wx.EVT_CLOSE, self.onClose)
        gif_file_name = "1.gif"
        panel = wx.Panel(self)
        box = wx.GridSizer(wx.HORIZONTAL)

        self.control = wx.TextCtrl(panel, size=(100, 100))

        close = wx.Button(panel, wx.ID_CLOSE, "Close")
        close.Bind(wx.EVT_BUTTON, self.onClose)

        self.check_box = wx.CheckBox(panel, label="mute")
        self.check_box.Bind(wx.EVT_CHECKBOX, self.OnPress, self.check_box)

        self.gif = wx.animate.GIFAnimationCtrl(self, id=-1, filename=gif_file_name, pos=(wx.Width, wx.Height))

        self.gif.Play()
        box.Add(self.control, 0, wx.ALL, 10)
        box.Add(self.check_box, 1, wx.ALL, 10)
        box.Add(close, 2, wx.ALL, 10)

        panel.SetSizer(box)
        panel.Show()

    def OnPress(self, event):
        if self.check_box.IsChecked():
            self.control.SetValue("I'm not listening to you")
        else:
            pass

    def onClose(self, event):
        dialog = wx.MessageDialog(self, "Do you really want to close this application?", "Confirm Exit",
                                  wx.OK | wx.CANCEL | wx.ICON_QUESTION)
        result = dialog.ShowModal()
        dialog.Destroy()
        if result == wx.ID_OK:
            self.Destroy()


app = wx.App()
frame = Frame()
frame.Show(True)
app.MainLoop()
