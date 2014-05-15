#Boa:Dialog:Dialog2

import wx

def create(parent):
    return Dialog2(parent)

[wxID_DIALOG2, wxID_DIALOG2LISTBOX1, wxID_DIALOG2LISTBOX2, 
 wxID_DIALOG2TREECTRL1, 
] = [wx.NewId() for _init_ctrls in range(4)]

class Dialog2(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG2, name='', parent=prnt,
              pos=wx.Point(623, 139), size=wx.Size(537, 485),
              style=wx.DEFAULT_DIALOG_STYLE, title='Dialog2')
        self.SetClientSize(wx.Size(521, 447))

        self.treeCtrl1 = wx.TreeCtrl(id=wxID_DIALOG2TREECTRL1, name='treeCtrl1',
              parent=self, pos=wx.Point(0, 24), size=wx.Size(192, 304),
              style=wx.TR_HAS_BUTTONS)

        self.listBox1 = wx.ListBox(choices=[], id=wxID_DIALOG2LISTBOX1,
              name='listBox1', parent=self, pos=wx.Point(192, 24),
              size=wx.Size(168, 304), style=0)

        self.listBox2 = wx.ListBox(choices=[], id=wxID_DIALOG2LISTBOX2,
              name='listBox2', parent=self, pos=wx.Point(360, 24),
              size=wx.Size(160, 304), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
