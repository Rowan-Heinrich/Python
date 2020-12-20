# Hello world program
"""
Hello World graphic - shown neatly
"""

import wx

class HelloFrame(wx.Frame):
    """
    A Frame that says Hello World
    """
    def __init__(self, *args, **kw):
        #Ensure the parents __init__ is called
        super(HelloFrame,self).__init__(*args, **kw)

        # create a panel in the frame
        pnl = wx.Panel(self)

        #put some text with a larger bold font on it.
        st = wx.StaticText(pnl,label="Loading ... ")
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

        # create a sizer to manage the layout of the widgets
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(st,wx.SizerFlags().Border(wx.TOP|wx.LEFT,25))
        pnl.SetSizer(sizer)

        #create menu bar:
        self.makeMenuBar()

        # create status bar:
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython")
        pass

    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected. 
        """
        #Make a file with Hello and Exit items
        fileMenu = wx.Menu()
        # the "/t..." syntax defines an accelerator key that also triggers the same event
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H",
                                    "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        # When using a stock ID we dont need to specify the menu items label
        exitItem = fileMenu.Append(wx.ID_EXIT)

        #Now a help menu for the about item:
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU Event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        pass

    def OnExit(self, event):
        """
        Close the frame, terminating the application
        """
        self.Close(True)

    def OnHello(self,event):
        """
        Say hello to the user
        """
        wx.MessageBox("Hello again form wxPython")

    def OnAbout(self, event):
        """
        Display an About dialog box
        """
        wx.MessageBox("This is a wxPython Hello World Sample",
                      "about hello world 2: ",
                      wx.OK|wx.ICON_INFORMATION)

if __name__ == '__main__':
    # when this module is run (not imported) then create
    # the app, the frame, show it, and start the event loop.
    app = wx.App()
    frm = HelloFrame(None, title='Hello World Application')
    frm.Show()
    app.MainLoop()
