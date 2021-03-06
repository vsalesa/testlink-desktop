#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import Frame1

modules ={'Dialog1': [0, '', u'Dialog1.py'],
 'Dialog2': [0, '', u'Dialog2.py'],
 'Dialog3': [0, '', u'Dialog3.py'],
 'Dialog4': [0, '', u'Dialog4.py'],
 'Frame1': [1, 'Main frame of Application', u'Frame1.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = Frame1.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
