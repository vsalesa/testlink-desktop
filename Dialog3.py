#Boa:Dialog:Dialog3

import wx
import Backend
import cPickle as pickle

def create(parent):
    return Dialog3(parent)

[wxID_DIALOG3, wxID_DIALOG3LISTBOX1, wxID_DIALOG3PLANLOADGAUGE, 
 wxID_DIALOG3STATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(4)]

class Dialog3(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG3, name='', parent=prnt,
              pos=wx.Point(637, 150), size=wx.Size(444, 355),
              style=wx.DEFAULT_DIALOG_STYLE, title='')
        self.SetClientSize(wx.Size(428, 317))

        self.staticText1 = wx.StaticText(id=wxID_DIALOG3STATICTEXT1,
              label='Select Test Plan', name='staticText1', parent=self,
              pos=wx.Point(8, 8), size=wx.Size(77, 13), style=0)

        self.listBox1 = wx.ListBox(choices=[], id=wxID_DIALOG3LISTBOX1,
              name='listBox1', parent=self, pos=wx.Point(8, 24),
              size=wx.Size(408, 264), style=0)
        self.listBox1.Bind(wx.EVT_LISTBOX, self.OnListBox1Listbox,
              id=wxID_DIALOG3LISTBOX1)

        self.PlanLoadGauge = wx.Gauge(id=wxID_DIALOG3PLANLOADGAUGE,
              name='PlanLoadGauge', parent=self, pos=wx.Point(8, 296),
              range=100, size=wx.Size(408, 16), style=wx.GA_HORIZONTAL)

    def __init__(self, parent):
        self._init_ctrls(parent)
        try:
            self.PickleLoad = pickle.load(open('SavedTestPlan.pkl', 'rb'))
            self.PlanList = self.PickleLoad.keys()
            self.listBox1.Set(self.PlanList)
        except:
            self.PickleLoad = "File does not exist..."
        
    def OnListBox1Listbox(self, event):
        selection = self.listBox1.GetSelection()
        CurrentPlan = self.PlanList[selection]
        self.CurrentPlanDetails = self.PickleLoad[CurrentPlan]
        #print self.CurrentPlanDetails
        cases = self.CurrentPlanDetails['cases']
        plan = self.CurrentPlanDetails['testplanid']
        i = 0
        total = len(cases)
        self.CaseList = []
        testplancases = Backend.GetCasesFromPlan(plan)
        #print testplancases.keys()
        #print testplancases
        for case in testplancases.keys():
            i = i + 1
            name = testplancases[case][0]['name']
            summary = testplancases[case][0]['summary']
            status = testplancases[case][0]['exec_status']
            self.CaseList.append([name, summary, status])
            progress = float(i)/float(total)
            progress = progress * 100.0
            self.PlanLoadGauge.SetValue(progress)
        #print "Case List: ", self.CaseList
        self.Destroy()
