import wx
import images

class MDIFrame(wx.MDIParentFrame):
    def __init__(self):
        wx.MDIParentFrame.__init__(self, None, -1, "MDI Parent", 
                size=(600,400))
        
        menu = wx.Menu()
        menu.Append(5000, "&New Window")
        menu.Append(5001, "&Upload Traffic")
        menu.Append(5002, "E&xit")
        menubar = wx.MenuBar()
        menubar.Append(menu, "&File")
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.OnNewWindow, id=5000)
        self.Bind(wx.EVT_MENU, self.OnExit, id=5002)
        
        # Status bar and Tool bar
        statusBar = self.CreateStatusBar()
        toolbar = self.CreateToolBar()
        toolbar.AddSimpleTool(wx.NewId(), images.getNewBitmap(),
                "New", "Long help for 'New'")
        toolbar.Realize()

    def OnExit(self, evt):
        self.Close(True)

    def OnNewWindow(self, evt):
        win = wx.MDIChildFrame(self, -1, "Child Window")
        win.Show(True)
        topLbl = wx.StaticText(win, -1, "Account Information")
        topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))

        nameLbl = wx.StaticText(win, -1, "Name:")
        name = wx.TextCtrl(win, -1, "");

        saveBtn = wx.Button(win, -1, "Save")
        cancelBtn = wx.Button(win, -1, "Cancel")


if __name__ == '__main__':
    app = wx.App(redirect=True)
    frame = MDIFrame()
    frame.Maximize()
    frame.Show()
    app.MainLoop()
        

