#Boa:Dialog:Dialog2

import wx

def create(parent):
    return Dialog2(parent)

[wxID_DIALOG2, wxID_DIALOG2BUTTON1, wxID_DIALOG2LISTBOX1, 
 wxID_DIALOG2LISTBOX2, wxID_DIALOG2STATICTEXT1, wxID_DIALOG2STATICTEXT2, 
 wxID_DIALOG2STATICTEXT3, wxID_DIALOG2SUMMARY, wxID_DIALOG2TEXTCTRL1, 
 wxID_DIALOG2TEXTCTRL2, 
] = [wx.NewId() for _init_ctrls in range(10)]

class Dialog2(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG2, name='', parent=prnt,
              pos=wx.Point(1663, -17), size=wx.Size(857, 485),
              style=wx.DEFAULT_DIALOG_STYLE, title='Test Case Title')
        self.SetClientSize(wx.Size(841, 447))

        self.listBox2 = wx.ListBox(choices=[], id=wxID_DIALOG2LISTBOX2,
              name='listBox2', parent=self, pos=wx.Point(8, 24),
              size=wx.Size(288, 192), style=0)

        self.listBox1 = wx.ListBox(choices=[], id=wxID_DIALOG2LISTBOX1,
              name='listBox1', parent=self, pos=wx.Point(296, 24),
              size=wx.Size(536, 192), style=0)

        self.staticText1 = wx.StaticText(id=wxID_DIALOG2STATICTEXT1,
              label='Test Case Title', name='staticText1', parent=self,
              pos=wx.Point(16, 8), size=wx.Size(72, 13), style=0)

        self.Summary = wx.StaticText(id=wxID_DIALOG2SUMMARY, label='Summary',
              name='Summary', parent=self, pos=wx.Point(304, 8),
              size=wx.Size(45, 13), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_DIALOG2TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(8, 240), size=wx.Size(288, 21), style=0,
              value='')

        self.textCtrl2 = wx.TextCtrl(id=wxID_DIALOG2TEXTCTRL2, name='textCtrl2',
              parent=self, pos=wx.Point(8, 288), size=wx.Size(824, 72), style=0,
              value='')

        self.staticText2 = wx.StaticText(id=wxID_DIALOG2STATICTEXT2,
              label='Test Case Title', name='staticText2', parent=self,
              pos=wx.Point(8, 224), size=wx.Size(72, 13), style=0)

        self.staticText3 = wx.StaticText(id=wxID_DIALOG2STATICTEXT3,
              label='Summary', name='staticText3', parent=self, pos=wx.Point(8,
              272), size=wx.Size(45, 13), style=0)

        self.button1 = wx.Button(id=wxID_DIALOG2BUTTON1, label='Add Test Case',
              name='button1', parent=self, pos=wx.Point(8, 368),
              size=wx.Size(144, 23), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
