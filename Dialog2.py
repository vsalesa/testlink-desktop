#Boa:Dialog:Dialog2

import wx
import Dialog1

def create(parent):
    return Dialog2(parent)

[wxID_DIALOG2, wxID_DIALOG2ADDCASETOPROJECT, wxID_DIALOG2CASESTOUPLOAD, 
 wxID_DIALOG2CASESUMMARY, wxID_DIALOG2CASETITLE, wxID_DIALOG2CURRENTSUITETEXT, 
 wxID_DIALOG2STATICTEXT2, wxID_DIALOG2STATICTEXT3, wxID_DIALOG2UPLOADCASES, 
] = [wx.NewId() for _init_ctrls in range(9)]

class Dialog2(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG2, name='', parent=prnt,
              pos=wx.Point(448, 62), size=wx.Size(857, 439),
              style=wx.DEFAULT_DIALOG_STYLE, title='Test Case Title')
        self.SetClientSize(wx.Size(841, 401))

        self.CasesToUpload = wx.ListBox(choices=[],
              id=wxID_DIALOG2CASESTOUPLOAD, name='CasesToUpload', parent=self,
              pos=wx.Point(8, 24), size=wx.Size(824, 192), style=0)
        self.CasesToUpload.Bind(wx.EVT_LISTBOX, self.OnCasesToUploadListbox,
              id=wxID_DIALOG2CASESTOUPLOAD)

        self.CurrentSuiteText = wx.StaticText(id=wxID_DIALOG2CURRENTSUITETEXT,
              label='Test Cases To Be Uploaded', name='CurrentSuiteText',
              parent=self, pos=wx.Point(16, 8), size=wx.Size(132, 13), style=0)

        self.CaseTitle = wx.TextCtrl(id=wxID_DIALOG2CASETITLE, name='CaseTitle',
              parent=self, pos=wx.Point(8, 240), size=wx.Size(288, 24), style=0,
              value='')

        self.CaseSummary = wx.TextCtrl(id=wxID_DIALOG2CASESUMMARY,
              name='CaseSummary', parent=self, pos=wx.Point(8, 288),
              size=wx.Size(824, 72), style=0, value='')

        self.staticText2 = wx.StaticText(id=wxID_DIALOG2STATICTEXT2,
              label='Test Case Title', name='staticText2', parent=self,
              pos=wx.Point(8, 224), size=wx.Size(72, 13), style=0)

        self.staticText3 = wx.StaticText(id=wxID_DIALOG2STATICTEXT3,
              label='Test Case Summary', name='staticText3', parent=self,
              pos=wx.Point(8, 272), size=wx.Size(96, 13), style=0)

        self.UploadCases = wx.Button(id=wxID_DIALOG2UPLOADCASES,
              label='Upload Test Cases', name='UploadCases', parent=self,
              pos=wx.Point(8, 368), size=wx.Size(216, 23), style=0)
        self.UploadCases.Bind(wx.EVT_BUTTON, self.OnUploadCasesButton,
              id=wxID_DIALOG2UPLOADCASES)

        self.AddCaseToProject = wx.Button(id=wxID_DIALOG2ADDCASETOPROJECT,
              label='Add Cases to Project', name='AddCaseToProject',
              parent=self, pos=wx.Point(240, 368), size=wx.Size(176, 23),
              style=0)
        self.AddCaseToProject.Bind(wx.EVT_BUTTON, self.OnAddCaseToProjectButton,
              id=wxID_DIALOG2ADDCASETOPROJECT)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.CaseTitle.SetFocus()
        self.CaseList = []
        self.CaseDisplay = []
        self.dlg1 = Dialog1.Dialog1(self)
        current = self.dlg1.CurrentProject
        
    def OnUploadCasesButton(self, event):
        case = self.CaseTitle.GetValue()
        summary = self.CaseSummary.GetValue()
        caseSummary = case + ': ' + summary
        self.CaseList.append((case, summary))
        self.CaseDisplay.append(caseSummary)
        self.CasesToUpload.Set(self.CaseDisplay)
        self.CaseTitle.SetLabel('')
        self.CaseSummary.SetLabel('')
        self.CaseTitle.SetFocus()

    def OnCasesToUploadListbox(self, event):
        event.Skip()

    def OnAddCaseToProjectButton(self, event):
        self.Destroy()
