import wx

def load(event):
    file = open(fileName.GetValue())
    contents.SetValue(file.read())
    file.close()

def save(event):
    file = open(fileName.GetValue(),'w')
    file.write(contents.GetValue())
    file.close()

app = wx.App()
win = wx.Frame(None, title="Intermediate Editor", size=(415,340))
bkg = wx.Panel(win)

fileName = wx.TextCtrl(bkg)
loadButton = wx.Button(bkg, label = "Open")
loadButton.Bind(wx.EVT_BUTTON,load)
saveButton = wx.Button(bkg, label = "Save")
saveButton.Bind(wx.EVT_BUTTON,save)
contents = wx.TextCtrl(bkg, value="Enter Text Here",style=wx.TE_MULTILINE | wx.HSCROLL)

hbox = wx.BoxSizer()
hbox.Add(fileName,proportion=2, flag=wx.EXPAND)
hbox.Add(saveButton, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(loadButton, proportion=0, flag=wx.LEFT, border=5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox,proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(contents, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT, border=5)

bkg.SetSizer(vbox)
win.Show()
app.MainLoop()
