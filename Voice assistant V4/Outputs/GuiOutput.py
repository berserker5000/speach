import platform
import wx
import wx.animate


class GUI(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(GUI, self).__init__(*args, **kwargs)

        self.MainUI()

    def MainUI(self):

        self.Bind(wx.EVT_CLOSE, self.onClose)

        self.SetSize((300, 200))
        self.SetTitle("Voice assistand for " + platform.system())
        self.Centre()
        self.Show(True)

        panel = wx.Panel(self)
        box = wx.GridSizer(wx.HORIZONTAL)

        # elements of visual form
        # close button
        close = wx.Button(panel, wx.ID_CLOSE, "Close")
        close.Bind(wx.EVT_BUTTON, self.onClose)

        # text field
        text = wx.TextCtrl(panel, pos=(150, 200))

        # multiline field with output
        label = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.SUNKEN_BORDER, size=(200, -1))

        # adding visual element to form
        box.Add(label, 1, wx.ALL, 3)
        box.Add(text, 1, wx.ALL, 3)
        box.Add(close, 2, wx.ALL, 3)

        panel.SetSizer(box)
        panel.Show()

    def onClose(self, event):
        dialog = wx.MessageDialog(self, "Do you really want to close this application?", "Confirm Exit",
                                  wx.OK | wx.CANCEL | wx.ICON_QUESTION)
        result = dialog.ShowModal()
        dialog.Destroy()
        if result == wx.ID_OK:
            self.Destroy()


class GiuOutput(object):
    def output(self):
        ex = wx.App()
        GUI(None)
        ex.MainLoop()


GiuOutput().output()