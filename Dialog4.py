#Boa:Dialog:Dialog4

import wx

def create(parent):
    return Dialog4(parent)

[wxID_DIALOG4, wxID_DIALOG4ADDSUITE, wxID_DIALOG4STATICTEXT1, 
 wxID_DIALOG4STATICTEXT2, wxID_DIALOG4SUITENAME, wxID_DIALOG4SUITESUMMARY, 
] = [wx.NewId() for _init_ctrls in range(6)]

class Dialog4(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG4, name='', parent=prnt,
              pos=wx.Point(456, 228), size=wx.Size(395, 207),
              style=wx.DEFAULT_DIALOG_STYLE, title='Create Suite')
        self.SetClientSize(wx.Size(379, 169))

        self.SuiteName = wx.TextCtrl(id=wxID_DIALOG4SUITENAME, name='SuiteName',
              parent=self, pos=wx.Point(8, 24), size=wx.Size(344, 21), style=0,
              value='')

        self.staticText1 = wx.StaticText(id=wxID_DIALOG4STATICTEXT1,
              label='Suite Name', name='staticText1', parent=self,
              pos=wx.Point(8, 8), size=wx.Size(55, 13), style=0)

        self.staticText2 = wx.StaticText(id=wxID_DIALOG4STATICTEXT2,
              label='Suite Summary', name='staticText2', parent=self,
              pos=wx.Point(8, 56), size=wx.Size(72, 13), style=0)

        self.SuiteSummary = wx.TextCtrl(id=wxID_DIALOG4SUITESUMMARY,
              name='SuiteSummary', parent=self, pos=wx.Point(8, 80),
              size=wx.Size(344, 56), style=0, value='')

        self.AddSuite = wx.Button(id=wxID_DIALOG4ADDSUITE,
              label='Add Suite To Project', name='AddSuite', parent=self,
              pos=wx.Point(8, 144), size=wx.Size(344, 23), style=0)
        self.AddSuite.Bind(wx.EVT_BUTTON, self.OnAddSuiteButton,
              id=wxID_DIALOG4ADDSUITE)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnAddSuiteButton(self, event):
        NameEntry = self.SuiteName.GetValue()
        SuiteEntry = self.SuiteSummary.GetValue()
        self.Entry = [NameEntry, SuiteEntry]
        self.Destroy()
