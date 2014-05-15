#Boa:Dialog:Dialog1

import wx
import Backend

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1CHECKBOX1, wxID_DIALOG1GETCASESBUTTON, 
 wxID_DIALOG1PANEL1, wxID_DIALOG1PLATFORMCHOICE, wxID_DIALOG1PLATFORMLABEL, 
 wxID_DIALOG1PROJECTCHOICE, wxID_DIALOG1PROJECTLABEL, 
 wxID_DIALOG1REARRANGECHECKBOX, wxID_DIALOG1TESTPLANCHOICE, 
 wxID_DIALOG1TESTPLANLABEL, 
] = [wx.NewId() for _init_ctrls in range(11)]

class Dialog1(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,
              pos=wx.Point(848, 205), size=wx.Size(296, 268),
              style=wx.DEFAULT_DIALOG_STYLE, title='Download Test Cases')
        self.SetClientSize(wx.Size(280, 230))

        self.panel1 = wx.Panel(id=wxID_DIALOG1PANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(288, 272),
              style=wx.TAB_TRAVERSAL)

        self.ProjectLabel = wx.StaticText(id=wxID_DIALOG1PROJECTLABEL,
              label='Project', name='ProjectLabel', parent=self.panel1,
              pos=wx.Point(8, 8), size=wx.Size(35, 13), style=0)

        self.ProjectChoice = wx.Choice(choices=[], id=wxID_DIALOG1PROJECTCHOICE,
              name='ProjectChoice', parent=self.panel1, pos=wx.Point(8, 24),
              size=wx.Size(264, 21), style=0)
        self.ProjectChoice.Bind(wx.EVT_CHOICE, self.OnProjectChoiceChoice,
              id=wxID_DIALOG1PROJECTCHOICE)

        self.TestPlanLabel = wx.StaticText(id=wxID_DIALOG1TESTPLANLABEL,
              label='TestPlan', name='TestPlanLabel', parent=self.panel1,
              pos=wx.Point(8, 56), size=wx.Size(42, 13), style=0)

        self.TestPlanChoice = wx.Choice(choices=[],
              id=wxID_DIALOG1TESTPLANCHOICE, name='TestPlanChoice',
              parent=self.panel1, pos=wx.Point(8, 72), size=wx.Size(264, 21),
              style=0)
        self.TestPlanChoice.Bind(wx.EVT_CHOICE, self.OnTestPlanChoiceChoice,
              id=wxID_DIALOG1TESTPLANCHOICE)

        self.PlatformLabel = wx.StaticText(id=wxID_DIALOG1PLATFORMLABEL,
              label='Platform', name='PlatformLabel', parent=self.panel1,
              pos=wx.Point(8, 104), size=wx.Size(41, 13), style=0)

        self.PlatformChoice = wx.Choice(choices=[],
              id=wxID_DIALOG1PLATFORMCHOICE, name='PlatformChoice',
              parent=self.panel1, pos=wx.Point(8, 120), size=wx.Size(264, 21),
              style=0)
        self.PlatformChoice.Bind(wx.EVT_CHOICE, self.OnPlatformChoiceChoice,
              id=wxID_DIALOG1PLATFORMCHOICE)

        self.GetCasesButton = wx.Button(id=wxID_DIALOG1GETCASESBUTTON,
              label='Get Test Cases', name='GetCasesButton', parent=self.panel1,
              pos=wx.Point(8, 200), size=wx.Size(264, 23), style=0)
        self.GetCasesButton.Bind(wx.EVT_BUTTON, self.OnGetCasesButtonButton,
              id=wxID_DIALOG1GETCASESBUTTON)

        self.RearrangeCheckBox = wx.CheckBox(id=wxID_DIALOG1REARRANGECHECKBOX,
              label='Rearrange execution order', name='RearrangeCheckBox',
              parent=self.panel1, pos=wx.Point(16, 152), size=wx.Size(248, 13),
              style=0)
        self.RearrangeCheckBox.SetValue(False)
        self.RearrangeCheckBox.SetToolTipString('Selecting this before you "Get Test Cases" will open a dialog window allowing the user to rearrange test cases.')

        self.checkBox1 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX1,
              label='Check for saved execution order', name='checkBox1',
              parent=self.panel1, pos=wx.Point(16, 176), size=wx.Size(192, 13),
              style=0)
        self.checkBox1.SetValue(True)

    def __init__(self, parent):
        self._init_ctrls(parent)
        Projects = Backend.GetProjects()
        self.ProjectIndex = []
        self.ProjectName = []
        self.CurrentProject = 'x'
        self.CurrentTestPlan = 'x'
        self.CurrentPlatform = 'x'
        for z in range(0, len(Projects)):
            self.ProjectIndex.append(Projects[z]['id'])
            self.ProjectName.append(Projects[z]['name'])
        self.ProjectChoice.SetItems(self.ProjectName)

    def OnProjectChoiceChoice(self, event):
        self.CurrentProject = self.ProjectChoice.GetSelection()
        TestPlans = Backend.GetTestPlans(self.ProjectIndex[self.CurrentProject])
        self.TestPlanIndex = []
        self.TestPlanName = []
        for z in range(0, len(TestPlans)):
            self.TestPlanIndex.append(TestPlans[z]['id'])
            self.TestPlanName.append(TestPlans[z]['name'])
        self.TestPlanChoice.SetItems(self.TestPlanName)

    def OnTestPlanChoiceChoice(self, event):
        self.CurrentTestPlan = self.TestPlanChoice.GetSelection()
        Platforms = Backend.GetPlatforms(self.TestPlanIndex[self.CurrentTestPlan])
        self.PlatformIndex = []
        self.PlatformName = []
        for z in range(0, len(Platforms)):
            self.PlatformIndex.append(Platforms[z]['id'])
            self.PlatformName.append(Platforms[z]['name'])
        self.PlatformChoice.SetItems(self.PlatformName)

    def OnPlatformChoiceChoice(self, event):
        self.CurrentPlatform = self.PlatformChoice.GetSelection()

    def OnGetCasesButtonButton(self, event):
        if self.CurrentProject != 'x' and self.CurrentTestPlan != 'x' and self.CurrentPlatform != 'x':
            self.DialogValues = [self.ProjectIndex[self.CurrentProject],
            self.TestPlanIndex[self.CurrentTestPlan],
            self.PlatformIndex[self.CurrentPlatform]]
            #print "Current Platform = ", self.CurrentPlatform
            #print self.DialogValues
            self.LoadCases()
            self.Destroy()
        else:
            print "Did not pass Button conditions..."
            print self.CurrentProject
            print self.CurrentTestPlan
            print self.CurrentPlatform
    
    def LoadCases(self):
        cases = Backend.GetCases(self.TestPlanIndex[self.CurrentTestPlan])
        self.CaseIndex = cases.keys()
        self.CaseList = []
        for case in cases.keys():
            #print "Name: ", cases[case][self.PlatformIndex[self.CurrentPlatform]]['name']
            #print "Summary: ", cases[case][self.PlatformIndex[self.CurrentPlatform]]['summary']
            #print "Status: ", cases[case][self.PlatformIndex[self.CurrentPlatform]]['exec_status']
            self.CaseList.append([cases[case][self.PlatformIndex[self.CurrentPlatform]]['name'],
                cases[case][self.PlatformIndex[self.CurrentPlatform]]['summary'],
                cases[case][self.PlatformIndex[self.CurrentPlatform]]['exec_status']])
                
                
        
        
            
            
