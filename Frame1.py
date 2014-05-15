#Boa:Frame:Frame1

import wx
import wx.html
import Backend
import Dialog1
import Dialog3

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BACKBUTTON, wxID_FRAME1BLOCKBUTTON, 
 wxID_FRAME1CASEGAUGE, wxID_FRAME1CASENAMELIST, wxID_FRAME1CASETRACKER, 
 wxID_FRAME1FAILBUTTON, wxID_FRAME1FORWARDBUTTON, wxID_FRAME1GETTESTCASES, 
 wxID_FRAME1HTMLWINDOW1, wxID_FRAME1LOADTESTPLAN, wxID_FRAME1PANEL1, 
 wxID_FRAME1PASSBUTTON, wxID_FRAME1SASHWINDOW1, wxID_FRAME1TESTCASENAME, 
 wxID_FRAME1TESTCOUNT, wxID_FRAME1WINDOW1, 
] = [wx.NewId() for _init_ctrls in range(17)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(362, 45), size=wx.Size(753, 266),
              style=wx.DEFAULT_FRAME_STYLE, title='TestLink Case Executor')
        self.SetClientSize(wx.Size(737, 228))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(737, 228),
              style=wx.TAB_TRAVERSAL)

        self.CaseNameList = wx.ListBox(choices=[], id=wxID_FRAME1CASENAMELIST,
              name='CaseNameList', parent=self.panel1, pos=wx.Point(0, 0),
              size=wx.Size(392, 120), style=0)
        self.CaseNameList.Bind(wx.EVT_LISTBOX, self.OnCaseNameListListbox,
              id=wxID_FRAME1CASENAMELIST)

        self.sashWindow1 = wx.SashWindow(id=wxID_FRAME1SASHWINDOW1,
              name='sashWindow1', parent=self.panel1, pos=wx.Point(392, 0),
              size=wx.Size(344, 120), style=wx.CLIP_CHILDREN | wx.SW_3D)

        self.TestCaseName = wx.StaticText(id=wxID_FRAME1TESTCASENAME, label='',
              name='TestCaseName', parent=self.sashWindow1, pos=wx.Point(16,
              16), size=wx.Size(240, 24), style=0)

        self.TestCount = wx.StaticText(id=wxID_FRAME1TESTCOUNT, label='',
              name='TestCount', parent=self.sashWindow1, pos=wx.Point(280, 16),
              size=wx.Size(53, 13), style=0)

        self.PassButton = wx.Button(id=wxID_FRAME1PASSBUTTON, label='PASS',
              name='PassButton', parent=self.sashWindow1, pos=wx.Point(48, 64),
              size=wx.Size(75, 23), style=0)
        self.PassButton.Bind(wx.EVT_BUTTON, self.OnPassButtonButton,
              id=wxID_FRAME1PASSBUTTON)

        self.FailButton = wx.Button(id=wxID_FRAME1FAILBUTTON, label='FAIL',
              name='FailButton', parent=self.sashWindow1, pos=wx.Point(136, 64),
              size=wx.Size(75, 23), style=0)
        self.FailButton.Bind(wx.EVT_BUTTON, self.OnFailButtonButton,
              id=wxID_FRAME1FAILBUTTON)

        self.BlockButton = wx.Button(id=wxID_FRAME1BLOCKBUTTON, label='BLOCK',
              name='BlockButton', parent=self.sashWindow1, pos=wx.Point(224,
              64), size=wx.Size(75, 23), style=0)
        self.BlockButton.Bind(wx.EVT_BUTTON, self.OnBlockButtonButton,
              id=wxID_FRAME1BLOCKBUTTON)

        self.BackButton = wx.Button(id=wxID_FRAME1BACKBUTTON, label='<-',
              name='BackButton', parent=self.sashWindow1, pos=wx.Point(16, 64),
              size=wx.Size(24, 23), style=0)
        self.BackButton.Bind(wx.EVT_BUTTON, self.OnBackButton,
              id=wxID_FRAME1BACKBUTTON)

        self.ForwardButton = wx.Button(id=wxID_FRAME1FORWARDBUTTON, label='->',
              name='ForwardButton', parent=self.sashWindow1, pos=wx.Point(312,
              64), size=wx.Size(24, 23), style=0)
        self.ForwardButton.Bind(wx.EVT_BUTTON, self.OnForwardButtonButton,
              id=wxID_FRAME1FORWARDBUTTON)

        self.window1 = wx.Window(id=wxID_FRAME1WINDOW1, name='window1',
              parent=self.panel1, pos=wx.Point(0, 120), size=wx.Size(736, 88),
              style=0)

        self.htmlWindow1 = wx.html.HtmlWindow(id=wxID_FRAME1HTMLWINDOW1,
              name='htmlWindow1', parent=self.window1, pos=wx.Point(0, 0),
              size=wx.Size(736, 100), style=wx.html.HW_SCROLLBAR_AUTO)

        self.GetTestCases = wx.Button(id=wxID_FRAME1GETTESTCASES,
              label='Create Test Plan', name='GetTestCases',
              parent=self.sashWindow1, pos=wx.Point(16, 96), size=wx.Size(152,
              23), style=0)
        self.GetTestCases.Bind(wx.EVT_BUTTON, self.OnGetTestCasesButton,
              id=wxID_FRAME1GETTESTCASES)

        self.CaseGauge = wx.Gauge(id=wxID_FRAME1CASEGAUGE, name='CaseGauge',
              parent=self.panel1, pos=wx.Point(8, 208), range=100,
              size=wx.Size(576, 16), style=wx.GA_HORIZONTAL)

        self.CaseTracker = wx.StaticText(id=wxID_FRAME1CASETRACKER, label='',
              name='CaseTracker', parent=self.panel1, pos=wx.Point(600, 208),
              size=wx.Size(0, 13), style=0)

        self.LoadTestPlan = wx.Button(id=wxID_FRAME1LOADTESTPLAN,
              label='Load Test Plan', name='LoadTestPlan',
              parent=self.sashWindow1, pos=wx.Point(184, 96), size=wx.Size(152,
              23), style=0)
        self.LoadTestPlan.Bind(wx.EVT_BUTTON, self.OnLoadTestPlanButton,
              id=wxID_FRAME1LOADTESTPLAN)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.CurrentCase = 0
        self.CaseList = []
        self.NameList = []
        
    def SetNameSummary(self, i):
        try:
            self.TestCaseName.SetLabel(self.CaseList[i][0])
            self.htmlWindow1.SetPage(self.CaseList[i][1])
            count = str(i+1) + "/" + str(len(self.CaseList)) + " cases"
            self.TestCount.SetLabel(count)
        except:
            print 'index: ', i, '       len of caselist: ', len(self.CaseList)
    
    def MoveForward(self):
        self.CurrentCase = self.CurrentCase + 1
        if self.CurrentCase > len(self.CaseList) - 1:
            self.CurrentCase = len(self.CaseList) - 1
        self.SetNameSummary(self.CurrentCase)
        self.CaseNameList.SetSelection(self.CurrentCase)
        
    def ShowNext(self):
        if self.CurrentCase == len(self.CaseIndex) - 1:
            print self.CurrentCase
            self.SetNameSummary(0)
            self.CaseNameList.SetSelection(0)
            return True
        else:
            print self.CurrentCase, "Else", len(self.CaseIndex)
            self.SetNameSummary(self.CurrentCase+1)
            self.CaseNameList.SetSelection(self.CurrentCase+1)
            return False
        
    def OnBackButton(self, event):
        if len(self.CaseList) == 0:
            self.OpenDialog()
        else:
            self.CurrentCase = self.CurrentCase - 1
            if self.CurrentCase < 0:
                self.CurrentCase = 0
            self.SetNameSummary(self.CurrentCase)
            self.CaseNameList.SetSelection(self.CurrentCase)

    def OnPassButtonButton(self, event):
        if len(self.CaseList) == 0:
            self.OpenDialog()
        else:
            begin = self.ShowNext()
            update = Backend.UpdateResult(self.CaseIndex[self.CurrentCase], self.CurrentTestPlan, 'p')
            print self.CaseIndex
            self.CaseNameList.SetItemBackgroundColour(self.CurrentCase, wx.Colour(0, 255, 128))
            self.CaseNameList.SetItemForegroundColour(self.CurrentCase, wx.Colour(0, 255, 128))
            modentry = self.CaseList[self.CurrentCase][0]
            modentry = '[P]' + modentry
            self.CaseNameList.SetString(self.CurrentCase, modentry)
            self.CurrentCase = self.CurrentCase+1
            if begin:
                self.CurrentCase = 0
            self.UpdateTestPlanResults(self.CurrentTestPlan)

    def OnFailButtonButton(self, event):
        if len(self.CaseList) == 0:
            self.OpenDialog()
        else:
            begin = self.ShowNext()
            update = Backend.UpdateResult(self.CaseIndex[self.CurrentCase], self.CurrentTestPlan, 'f')
            self.CaseNameList.SetItemBackgroundColour(self.CurrentCase, wx.Colour(0, 255, 128))
            self.CaseNameList.SetItemForegroundColour(self.CurrentCase, wx.Colour(0, 255, 128))
            modentry = self.CaseList[self.CurrentCase][0]
            modentry = '[F]' + modentry
            self.CaseNameList.SetString(self.CurrentCase, modentry)
            self.CurrentCase = self.CurrentCase+1
            if begin:
                self.CurrentCase = 0
            self.UpdateTestPlanResults(self.CurrentTestPlan)

    def OnBlockButtonButton(self, event):
        if len(self.CaseList) == 0:
            self.OpenDialog()
        else:
            begin = self.ShowNext()
            update = Backend.UpdateResult(self.CaseIndex[self.CurrentCase], self.CurrentTestPlan, 'b')
            self.CaseNameList.SetItemBackgroundColour(self.CurrentCase, wx.Colour(0, 255, 128))
            self.CaseNameList.SetItemForegroundColour(self.CurrentCase, wx.Colour(0, 255, 128))
            modentry = self.CaseList[self.CurrentCase][0]
            modentry = '[B]' + modentry
            self.CaseNameList.SetString(self.CurrentCase, modentry)
            self.CurrentCase = self.CurrentCase+1
            if begin:
                self.CurrentCase = 0
            self.UpdateTestPlanResults(self.CurrentTestPlan)

    def OnForwardButtonButton(self, event):
        if len(self.CaseList) == 0:
            self.OpenDialog()
        else:
            self.MoveForward()

    def OnCaseNameListListbox(self, event):
        self.CurrentCase = self.CaseNameList.GetSelection()
        self.SetNameSummary(self.CurrentCase)

    def OnGetTestCasesButton(self, event):
        self.OpenDialog()
        
    def UpdateTestPlanResults(self, planid):
        results = Backend.UpdateTotals(planid)
        print "Test Plan Results: ", results
        total = results[0]['total_tc']
        not_run = results[0]['details']['not_run']['qty']
        result_text = str(not_run) + " of " + str(total) + " not run..."
        self.CaseTracker.SetLabel(result_text)
        total = float(total)
        not_run = float(not_run)
        result_percent = ((total-not_run)/total)*100.0
        self.CaseGauge.SetValue(result_percent)
        
    def OpenDialog(self):
        self.dlg = Dialog1.Dialog1(self)
        try:
            self.dlg.ShowModal()
        finally:
            pass
##            try:
##                self.CaseIndex = self.dlg.CaseIndex
##                self.CaseList = self.dlg.CaseList
##                self.DialogValues = self.dlg.DialogValues
##                print 'Dialog Values: ', self.DialogValues, '     project, plan, platform'
##                self.CurrentProject = self.DialogValues[0]
##                self.CurrentTestPlan = self.DialogValues[1]
##                self.CurrentPlatform = self.DialogValues[2]
##                self.NameList = []
##                for entry in self.CaseList:
##                    if entry[2] == 'n':
##                        modentry = '[_]'+entry[0]
##                        
##                    elif entry[2] == 'p':
##                        modentry = '[P]' + entry[0]
##                        
##                    elif entry[2] == 'f':
##                        modentry = '[F]' + entry[0]
##                        
##                    elif entry[2] == 'b':
##                        modentry = '[B]' + entry[0]
##                    else:
##                        print "It didn't work!!!"
##                    self.NameList.append(modentry)
##                self.SetNameSummary(self.CurrentCase)
##                self.CaseNameList.Set(self.NameList)
##                self.CaseNameList.SetSelection(0)
##                self.UpdateTestPlanResults(self.CurrentTestPlan)
##                self.dlg.Destroy()
##            finally:
##                pass
            
    def OnLoadTestPlanButton(self, event):
        self.OpenLoadDialog()
    
    def OpenLoadDialog(self):
        print "Opening dialog..."
        self.dlg3 = Dialog3.Dialog3(self)
        try:
            self.dlg3.ShowModal()
        finally:
            try:
                
                self.CurrentPlanDetails = self.dlg3.CurrentPlanDetails
                print "Test Case Selected..."
                self.CaseList = self.dlg3.CaseList
                print self.CurrentPlanDetails
                self.CurrentTestPlan = self.CurrentPlanDetails['testplanid']
                self.CaseIndex = self.CurrentPlanDetails['cases']
                self.CurrentProject = self.CurrentPlanDetails['project']
                self.NameList = []
                for entry in self.CaseList:
                    print "Entry ", entry
                    if entry[2] == 'n':
                        modentry = '[_]'+entry[0]
                        
                    elif entry[2] == 'p':
                        modentry = '[P]' + entry[0]
                        
                    elif entry[2] == 'f':
                        modentry = '[F]' + entry[0]
                        
                    elif entry[2] == 'b':
                        modentry = '[B]' + entry[0]
                    else:
                        print "It didn't work!!!"
                    self.NameList.append(modentry)
                self.SetNameSummary(self.CurrentCase)
                self.CaseNameList.Set(self.NameList)
                self.CaseNameList.SetSelection(0)
                self.UpdateTestPlanResults(self.CurrentTestPlan)
            except:
                print "There was no data..."
            
            
