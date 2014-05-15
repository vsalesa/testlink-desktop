#Boa:Dialog:Dialog1

import wx
import wx.html
import Backend
import Dialog3
import cPickle as pickle

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1APPENDTESTPLAN, wxID_DIALOG1CASELIST, 
 wxID_DIALOG1CASESLABEL, wxID_DIALOG1CREATECASEBUTTON, 
 wxID_DIALOG1CREATESUITEBUTTON, wxID_DIALOG1CURRENTSUITELABEL, 
 wxID_DIALOG1EXECUTIONLIST, wxID_DIALOG1GETPROJECTBUTTON, 
 wxID_DIALOG1HTMLWINDOW1, wxID_DIALOG1INPUTLABEL, wxID_DIALOG1LOADTESTPLAN, 
 wxID_DIALOG1PANEL1, wxID_DIALOG1PLANNAME, wxID_DIALOG1PROJECTCHOICE, 
 wxID_DIALOG1PROJECTLABEL, wxID_DIALOG1QUEUECOUNTDISPLAY, 
 wxID_DIALOG1QUEUELABEL, wxID_DIALOG1SAVEPLANBUTTON, wxID_DIALOG1SAVINGGAUGE, 
 wxID_DIALOG1STATICLINE1, wxID_DIALOG1STATICLINE2, wxID_DIALOG1STATICLINE3, 
 wxID_DIALOG1STATICLINE4, wxID_DIALOG1STATICLINE5, wxID_DIALOG1SUITESLABEL, 
 wxID_DIALOG1SUITESLIST, wxID_DIALOG1SUMMARYLABEL, 
] = [wx.NewId() for _init_ctrls in range(28)]

class Dialog1(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,
              pos=wx.Point(652, 33), size=wx.Size(701, 686),
              style=wx.DEFAULT_DIALOG_STYLE, title='Create Test Plan')
        self.SetClientSize(wx.Size(685, 648))

        self.panel1 = wx.Panel(id=wxID_DIALOG1PANEL1, name='panel1',
              parent=self, pos=wx.Point(8, 8), size=wx.Size(688, 536),
              style=wx.TAB_TRAVERSAL)

        self.ProjectLabel = wx.StaticText(id=wxID_DIALOG1PROJECTLABEL,
              label='Project', name='ProjectLabel', parent=self.panel1,
              pos=wx.Point(0, 8), size=wx.Size(43, 13), style=0)

        self.ProjectChoice = wx.Choice(choices=[], id=wxID_DIALOG1PROJECTCHOICE,
              name='ProjectChoice', parent=self.panel1, pos=wx.Point(48, 8),
              size=wx.Size(520, 21), style=0)
        self.ProjectChoice.Bind(wx.EVT_CHOICE, self.OnProjectChoice,
              id=wxID_DIALOG1PROJECTCHOICE)

        self.GetProjectButton = wx.Button(id=wxID_DIALOG1GETPROJECTBUTTON,
              label='Get Project', name='GetProjectButton', parent=self.panel1,
              pos=wx.Point(576, 8), size=wx.Size(88, 24), style=0)
        self.GetProjectButton.Bind(wx.EVT_BUTTON, self.OnGetProjectsButton,
              id=wxID_DIALOG1GETPROJECTBUTTON)

        self.staticLine1 = wx.StaticLine(id=wxID_DIALOG1STATICLINE1,
              name='staticLine1', parent=self.panel1, pos=wx.Point(9, 72),
              size=wx.Size(655, 2), style=0)

        self.SuitesList = wx.ListBox(choices=[], id=wxID_DIALOG1SUITESLIST,
              name='SuitesList', parent=self.panel1, pos=wx.Point(8, 104),
              size=wx.Size(232, 312), style=0)
        self.SuitesList.Bind(wx.EVT_LISTBOX, self.OnSuitesListListbox,
              id=wxID_DIALOG1SUITESLIST)

        self.CaseList = wx.ListBox(choices=[], id=wxID_DIALOG1CASELIST,
              name='CaseList', parent=self.panel1, pos=wx.Point(240, 104),
              size=wx.Size(224, 312), style=0)
        self.CaseList.Bind(wx.EVT_LISTBOX, self.OnCaseListListbox,
              id=wxID_DIALOG1CASELIST)
        self.CaseList.Bind(wx.EVT_LISTBOX_DCLICK, self.OnCaseListListboxDclick,
              id=wxID_DIALOG1CASELIST)

        self.ExecutionList = wx.ListBox(choices=[],
              id=wxID_DIALOG1EXECUTIONLIST, name='ExecutionList',
              parent=self.panel1, pos=wx.Point(464, 104), size=wx.Size(200,
              312), style=0)
        self.ExecutionList.Bind(wx.EVT_LISTBOX, self.OnExecutionListListbox,
              id=wxID_DIALOG1EXECUTIONLIST)
        self.ExecutionList.Bind(wx.EVT_LISTBOX_DCLICK,
              self.OnExecutionListListboxDclick, id=wxID_DIALOG1EXECUTIONLIST)

        self.SuitesLabel = wx.StaticText(id=wxID_DIALOG1SUITESLABEL,
              label='Test Suites', name='SuitesLabel', parent=self.panel1,
              pos=wx.Point(72, 80), size=wx.Size(91, 23), style=0)
        self.SuitesLabel.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.SuitesLabel.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.CasesLabel = wx.StaticText(id=wxID_DIALOG1CASESLABEL,
              label='Test Cases', name='CasesLabel', parent=self.panel1,
              pos=wx.Point(304, 80), size=wx.Size(88, 23), style=0)
        self.CasesLabel.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.QueueLabel = wx.StaticText(id=wxID_DIALOG1QUEUELABEL,
              label='Execution Queue', name='QueueLabel', parent=self.panel1,
              pos=wx.Point(488, 80), size=wx.Size(142, 23), style=0)
        self.QueueLabel.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.SummaryLabel = wx.StaticText(id=wxID_DIALOG1SUMMARYLABEL,
              label='Summary', name='SummaryLabel', parent=self.panel1,
              pos=wx.Point(8, 432), size=wx.Size(45, 13), style=0)

        self.staticLine2 = wx.StaticLine(id=wxID_DIALOG1STATICLINE2,
              name='staticLine2', parent=self.panel1, pos=wx.Point(32, 432),
              size=wx.Size(1, 2), style=0)

        self.staticLine3 = wx.StaticLine(id=wxID_DIALOG1STATICLINE3,
              name='staticLine3', parent=self.panel1, pos=wx.Point(8, 424),
              size=wx.Size(656, 2), style=0)

        self.CreateSuiteButton = wx.Button(id=wxID_DIALOG1CREATESUITEBUTTON,
              label='Create Suite', name='CreateSuiteButton', parent=self,
              pos=wx.Point(24, 552), size=wx.Size(216, 24), style=0)

        self.CreateCaseButton = wx.Button(id=wxID_DIALOG1CREATECASEBUTTON,
              label='Create Test Cases', name='CreateCaseButton', parent=self,
              pos=wx.Point(256, 552), size=wx.Size(208, 23), style=0)
        self.CreateCaseButton.Bind(wx.EVT_BUTTON, self.OnCreateCaseButtonButton,
              id=wxID_DIALOG1CREATECASEBUTTON)

        self.staticLine4 = wx.StaticLine(id=wxID_DIALOG1STATICLINE4,
              name='staticLine4', parent=self, pos=wx.Point(248, 552),
              size=wx.Size(1, 128), style=0)

        self.staticLine5 = wx.StaticLine(id=wxID_DIALOG1STATICLINE5,
              name='staticLine5', parent=self, pos=wx.Point(472, 552),
              size=wx.Size(1, 128), style=0)

        self.SavePlanButton = wx.Button(id=wxID_DIALOG1SAVEPLANBUTTON,
              label='Save Test Plan', name='SavePlanButton', parent=self,
              pos=wx.Point(480, 584), size=wx.Size(192, 23), style=0)
        self.SavePlanButton.Bind(wx.EVT_BUTTON, self.OnSavePlanButtonButton,
              id=wxID_DIALOG1SAVEPLANBUTTON)

        self.htmlWindow1 = wx.html.HtmlWindow(id=wxID_DIALOG1HTMLWINDOW1,
              name='htmlWindow1', parent=self.panel1, pos=wx.Point(8, 448),
              size=wx.Size(656, 88), style=wx.html.HW_SCROLLBAR_AUTO)

        self.CurrentSuiteLabel = wx.StaticText(id=wxID_DIALOG1CURRENTSUITELABEL,
              label='Select Project', name='CurrentSuiteLabel',
              parent=self.panel1, pos=wx.Point(16, 56), size=wx.Size(67, 13),
              style=0)

        self.QueueCountDisplay = wx.StaticText(id=wxID_DIALOG1QUEUECOUNTDISPLAY,
              label='', name='QueueCountDisplay', parent=self.panel1,
              pos=wx.Point(616, 56), size=wx.Size(40, 13), style=0)

        self.PlanName = wx.TextCtrl(id=wxID_DIALOG1PLANNAME, name='PlanName',
              parent=self, pos=wx.Point(480, 560), size=wx.Size(192, 21),
              style=0, value='')

        self.InputLabel = wx.StaticText(id=wxID_DIALOG1INPUTLABEL,
              label='Test Plan Name', name='InputLabel', parent=self,
              pos=wx.Point(488, 544), size=wx.Size(75, 13), style=0)

        self.SavingGauge = wx.Gauge(id=wxID_DIALOG1SAVINGGAUGE,
              name='SavingGauge', parent=self, pos=wx.Point(480, 632),
              range=100, size=wx.Size(192, 8), style=wx.GA_HORIZONTAL)

        self.LoadTestPlan = wx.Button(id=wxID_DIALOG1LOADTESTPLAN,
              label='Load Test Plan', name='LoadTestPlan', parent=self,
              pos=wx.Point(576, 608), size=wx.Size(96, 23), style=0)
        self.LoadTestPlan.Bind(wx.EVT_BUTTON, self.OnLoadTestPlanButton,
              id=wxID_DIALOG1LOADTESTPLAN)

        self.AppendTestPlan = wx.Button(id=wxID_DIALOG1APPENDTESTPLAN,
              label='Append Test Plan', name='AppendTestPlan', parent=self,
              pos=wx.Point(480, 608), size=wx.Size(96, 24), style=0)
        self.AppendTestPlan.Bind(wx.EVT_BUTTON, self.OnAppendTestPlanButton,
              id=wxID_DIALOG1APPENDTESTPLAN)

    def __init__(self, parent):
        self._init_ctrls(parent)
        Projects = Backend.GetProjects()
        #print "Projects: "
        #print Projects
        self.ProjectIndex = []
        self.ProjectName = []
        self.ProjectPrefix = []
        self.CurrentProject = 'x'
        self.CurrentProjectPrefix = 'x'
        self.CurrentTestPlan = 'x'
        self.CurrentPlatform = 'x'
        self.LoadQueueList = []
        self.LoadQueueIDList = []
        for z in range(0, len(Projects)):
            self.ProjectIndex.append(Projects[z]['id'])
            self.ProjectName.append(Projects[z]['name'])
            self.ProjectPrefix.append(Projects[z]['prefix'])
        self.ProjectChoice.SetItems(self.ProjectName)
 
    def OnProjectChoice(self, event):
        event.Skip()

    def OnGetProjectsButton(self, event):
        self.QueueList = []
        self.QueueIDList = []
        self.CasesList = []
        self.CasesIDList = []
        self.ExecutionList.Set(self.QueueList)
        self.CaseList.Set(self.CasesList)
        selection = self.ProjectChoice.GetSelection()
        #print self.ProjectIndex
        self.CurrentProject = self.ProjectIndex[selection]
        self.CurrentProjectName = self.ProjectName[selection]
        self.CurrentProjectPrefix = self.ProjectPrefix[selection]
        self.CurrentCount = Backend.GetCaseCountForProject(self.CurrentProjectName)
        #print self.CurrentCount
        self.UpdateQueueCount()
        #print self.CurrentProject
        Suites = Backend.GetSuitesInProject(self.CurrentProject)
        #print Suites
        self.SuiteList = []
        self.SuiteIDList = []
        for suite in Suites:
            #print suite['name']
            self.SuiteList.append(suite['name'])
            self.SuiteIDList.append(suite['id'])
        self.SuitesList.Set(self.SuiteList)
        self.RankTracker = [self.ProjectName[selection]]
        self.RankIDTracker = [self.ProjectIndex[selection]]
        self.UpdateSuiteListLabel()
        choice = self.ExecutionList.GetSelection()
        #print "Choice = ", choice
        

    def OnSuitesListListbox(self, event):
        index = self.SuitesList.GetSelection()
        self.CurrentSuite = self.SuiteList[index]
        self.CurrentSuiteID = self.SuiteIDList[index]
        self.CasesList = []
        self.CasesIDList = []
        
        if self.CurrentSuite == '..':
            self.RankTracker.pop(len(self.RankTracker)-1)
            self.RankIDTracker.pop(len(self.RankIDTracker)-1)
            if len(self.RankIDTracker) == 1:
                Suites = Backend.GetSuitesInProject(self.CurrentProject)
                self.SuiteList = []
                self.SuiteIDList = []
                for suite in Suites:
                    #print suite['name']
                    self.SuiteList.append(suite['name'])
                    self.SuiteIDList.append(suite['id'])
            else:
                self.CurrentSuite = self.RankTracker[-1]
                self.CurrentSuiteID = self.RankIDTracker[-1]
                #print 'Popped...', self.CurrentSuiteID, self.CurrentSuite
                #print "Current Suite ID: ", self.CurrentSuiteID
                Suites = Backend.GetSuitesInSuite(self.CurrentSuiteID)
                Cases = Backend.GetCasesInSuite(self.CurrentSuiteID)
                self.SuiteList = ['..']
                self.SuiteIDList = ['..']
                self.CasesList = []
                self.CasesIDList = []
                if Suites != '':
                    list = Suites.keys()
                    if list[0] == 'node_type_id':
                        #print "Setting single suite..."
                        #print Suites['name'], Suites['id']
                        self.SuiteList.append(Suites['name'])
                        self.SuiteIDList.append(Suites['id'])
                    else:
                        for suite in Suites:
                            #print "Suite list...", suite
                            self.SuiteList.append(Suites[suite]['name'])
                            self.SuiteIDList.append(Suites[suite]['id'])
                #print "Suites"
                #print Suites
                #print self.SuiteList, self.SuiteIDList
                
                for z in range(0, len(Cases)-1):
                    if Cases[z]['id'] in self.QueueIDList:
                        pass
                    else:
                        #print "Appending... ", Cases[z]['id'], Cases[z]['name']
                        self.CasesList.append(Cases[z]['name'])
                        self.CasesIDList.append(Cases[z]['id'])
        else:
            Suites = []
            self.RankTracker.append(self.CurrentSuite)
            self.RankIDTracker.append(self.CurrentSuiteID)
            Suites = Backend.GetSuitesInSuite(self.CurrentSuiteID)
            Cases = Backend.GetCasesInSuite(self.CurrentSuiteID)
            self.SuiteList = ['..']
            self.SuiteIDList = ['..']
            self.CasesList = []
            self.CasesIDList = []
            #print "Suites before list...", Suites
            if Suites != '':
                list = Suites.keys()
                if list[0] == 'node_type_id':
                    #print "Setting single suite..."
                    #print Suites['name'], Suites['id']
                    self.SuiteList.append(Suites['name'])
                    self.SuiteIDList.append(Suites['id'])
                else:
                    for suite in Suites:
                        #print "Suite list...", suite
                        self.SuiteList.append(Suites[suite]['name'])
                        self.SuiteIDList.append(Suites[suite]['id'])
            #print "Suites"
            #print Suites
            #print self.SuiteList, self.SuiteIDList
            #print Cases
            for z in range(0, len(Cases)):
                if Cases[z]['id'] in self.QueueIDList:
                    pass
                else:
                    #print "Appending... ", Cases[z]['id'], Cases[z]['name']
                    self.CasesList.append(Cases[z]['name'])
                    self.CasesIDList.append(Cases[z]['id'])
                    #print "Turn #", z
            #print self.CasesList
        
        #print 'Suites: ', Suites
        
                
        self.SuitesList.Set(self.SuiteList)
        self.CaseList.Set(self.CasesList)
        self.UpdateSuiteListLabel()
            
    def UpdateSuiteListLabel(self):
        current_suite = ''
        for rank in self.RankTracker:
            current_suite = current_suite + rank + '/'
        #print current_suite
        self.CurrentSuiteLabel.SetLabel(current_suite)

    def OnCaseListListbox(self, event):
        choice = self.CaseList.GetSelection()
        caseid = self.CasesIDList[choice]
        summary = Backend.GetSummary(caseid)
        summary = summary[0]['summary']
        self.htmlWindow1.SetPage(summary)

    def OnCaseListListboxDclick(self, event):
        choice = self.CaseList.GetSelection()
        ex_choice = self.ExecutionList.GetSelection()
        if ex_choice == -1:
            self.QueueList.append(self.CasesList[choice])
            self.QueueIDList.append(self.CasesIDList[choice])
            selection = len(self.QueueList) - 1
        else:
            self.QueueList.insert(ex_choice+1, self.CasesList[choice])
            self.QueueIDList.insert(ex_choice+1, self.CasesIDList[choice])
            selection = ex_choice+1
        self.ExecutionList.Set(self.QueueList)
        self.ExecutionList.SetSelection(selection)
        self.CasesList.pop(choice)
        self.CasesIDList.pop(choice)
        self.CaseList.Set(self.CasesList)
        self.UpdateQueueCount()
        
    def OnExecutionListListbox(self, event):
        choice = self.ExecutionList.GetSelection()
        caseid = self.QueueIDList[choice]
        summary = Backend.GetSummary(caseid)
        summary = summary[0]['summary']
        self.htmlWindow1.SetPage(summary)

    def OnExecutionListListboxDclick(self, event):
        choice = self.ExecutionList.GetSelection()
        self.QueueList.pop(choice)
        self.QueueIDList.pop(choice)
        self.ExecutionList.Set(self.QueueList)
        if choice > len(self.QueueList)-1:
            self.ExecutionList.SetSelection(choice-1)
        else:
            self.ExecutionList.SetSelection(choice)
        self.UpdateQueueCount()
    
    def UpdateQueueCount(self):
        count = str(len(self.QueueList))
        count = count + "/" + self.CurrentCount
        self.QueueCountDisplay.SetLabel(count)

    def OnSavePlanButtonButton(self, event):
        self.InputLabel.SetLabel('Saving Test Cases...')
        name = self.PlanName.GetValue()
        pickname = name
        try:
            PickleLoad = pickle.load(open('SavedTestPlan.pkl', 'rb'))
        except:
            PickleLoad = {}
        #print "Pickle Load: ", PickleLoad
        name = "*API* " + name
        #print name
        #print self.CurrentProjectName
        #print "Prefix=",self.CurrentProjectPrefix
        response = Backend.CreateTestPlan(name, self.CurrentProjectName)
        #print response
        response_id = response[0]['id']
        response = Backend.CreateBuild(response_id, "Auto Build",
            "This build was created automatically by the API to avoid execution issues...")
        #print "Build creation response...", response
        #print "Response ID: ", response_id
        i = 0
        for case in self.QueueIDList:
            summary = Backend.GetCaseFromID(case)
            #print case, ":", summary
            external_id = summary[0]['tc_external_id']
            external_id = self.CurrentProjectPrefix + "-" + external_id
            #print "New external id...", external_id
            version = summary[0]['version']
            version = int(version)
            #print "external id, version", external_id, version
            print "args = ", (self.CurrentProject,
                        response_id, external_id, version)
            response = Backend.AddCaseToTestPlan(self.CurrentProject,
                        response_id, external_id, version)
            #print response
            i = i + 1
            total = len(self.QueueIDList)
            
            progress = float(i)/float(total)
            progress = progress * 100.0
            #print progress
            self.SavingGauge.SetValue(progress)
        PlanPickle = {'testplanid':response_id,
                        'cases': self.QueueIDList,
                        'project': self.CurrentProject }
        PickleLoad[pickname] = PlanPickle
        #print "Plan Pickle", PlanPickle
        pickle.dump(PickleLoad, open('SavedTestPlan.pkl', 'wb'))
        self.SavingGauge.SetValue(0)
        self.InputLabel.SetLabel('Test Case Name')

    def OnCreateCaseButtonButton(self, event):
        self.dlg2 = Dialog2.Dialog2(self)

    def OnLoadTestPlanButton(self, event):
        #print "Current Project", self.CurrentProject
        self.dlg3 = Dialog3.Dialog3(self)
        try:
            self.dlg3.ShowModal()
        finally:
            try:
                self.CurrentPlanDetails = self.dlg3.CurrentPlanDetails
                self.CasesList = self.dlg3.CaseList
                #print self.CurrentPlanDetails
                self.QueueList = []
                self.QueueIDList = []
                self.CasesList = []
                self.CasesIDList = []
                self.ExecutionList.Set(self.QueueList)
                self.CaseList.Set(self.CasesList)
                self.CurrentProject = self.CurrentPlanDetails['project']
                self.CurrentProjectName = self.ProjectName[self.ProjectIndex.index(self.CurrentProject)]
                self.CurrentProjectPrefix = self.ProjectPrefix[self.ProjectIndex.index(self.CurrentProject)]
                self.CurrentCount = Backend.GetCaseCountForProject(self.CurrentProjectName)
                Suites = Backend.GetSuitesInProject(self.CurrentProject)
                self.SuiteList = []
                self.SuiteIDList = []
                for suite in Suites:
                    #print suite['name']
                    self.SuiteList.append(suite['name'])
                    self.SuiteIDList.append(suite['id'])
                self.SuitesList.Set(self.SuiteList)
                self.RankTracker = [self.CurrentProjectName]
                self.RankIDTracker = [self.CurrentProject]
                self.UpdateSuiteListLabel()
                choice = self.ExecutionList.GetSelection()
                self.QueueIDList = self.CurrentPlanDetails['cases']
                self.QueueList = []
                plan = self.CurrentPlanDetails['testplanid']
                testplancases = Backend.GetCasesFromPlan(plan)
                for i in self.QueueIDList:
                    #print i
                    self.QueueList.append(testplancases[i][0]['name'])
                #print self.CurrentProjectName, self.CurrentProjectPrefix
                #print self.QueueList
                self.LoadQueueList = self.QueueList
                self.LoadQueueIDList = self.QueueIDList
                self.ExecutionList.Set(self.QueueList)
                
                self.UpdateQueueCount()
                
                
            finally:
                pass

    def OnAppendTestPlanButton(self, event):
        print "Current Project", self.CurrentProject
        self.dlg3 = Dialog3.Dialog3(self)
        try:
            self.dlg3.ShowModal()
        finally:
            try:
                self.CurrentPlanDetails = self.dlg3.CurrentPlanDetails
                self.CasesList = self.dlg3.CaseList
                self.CurrentPlan = self.dlg3.CurrentPlan
                print self.CurrentPlanDetails
                print "LoadQueueIDList", self.LoadQueueIDList
                print "LoadQueueIDList", self.QueueIDList
                NewCaseList = []
                i = 0
                response_id = self.CurrentPlanDetails['testplanid']
                cases = self.CurrentPlanDetails['cases']
                if self.CurrentProject == self.CurrentPlanDetails['project']:
                    for case in self.LoadQueueIDList:
                        if case in cases:
                            pass
                            print "Passed case #", case
                        else:
                            summary = Backend.GetCaseFromID(case)
                            external_id = summary[0]['tc_external_id']
                            external_id = self.CurrentProjectPrefix + "-" + external_id
                            version = summary[0]['version']
                            version = int(version)
                            print "Appending case #", case
                            response = Backend.AddCaseToTestPlan(self.CurrentProject,
                                        response_id, external_id, version)
                        i = i + 1
                        total = len(self.LoadQueueIDList)
                        progress = float(i)/float(total)
                        progress = progress * 100.0
                        self.SavingGauge.SetValue(progress)
                    PickleLoad = pickle.load(open('SavedTestPlan.pkl', 'rb'))
                    PickleLoad[self.CurrentPlan]['cases'] = self.QueueIDList
                    pickle.dump(PickleLoad, open('SavedTestPlan.pkl', 'wb'))
                    self.SavingGauge.SetValue(0)
                    self.InputLabel.SetLabel('Test Case Name') 
                            
                            
                            
            finally:
                pass
                    
        
        
            
            
