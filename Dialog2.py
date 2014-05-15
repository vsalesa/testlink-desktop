#Boa:Dialog:Dialog2

import wx

def create(parent):
    return Dialog2(parent)

[wxID_DIALOG2, wxID_DIALOG2LISTBOX2, 
] = [wx.NewId() for _init_ctrls in range(2)]

class Dialog2(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG2, name='', parent=prnt,
              pos=wx.Point(623, 139), size=wx.Size(522, 485),
              style=wx.DEFAULT_DIALOG_STYLE, title='Dialog2')
        self.SetClientSize(wx.Size(506, 447))

        self.listBox2 = wx.ListBox(choices=[], id=wxID_DIALOG2LISTBOX2,
              name='listBox2', parent=self, pos=wx.Point(16, 16),
              size=wx.Size(472, 192), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
