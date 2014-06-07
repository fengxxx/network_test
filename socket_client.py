#!/usr/bin/env python
import  socket
import wx
HOST="localhost"
PORT=56219

MAIN_BG_COLOR=(37,37,37)
ALLMSG=" "
#SEND_MSG=""
NAME="client_01"


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


i=1
 
class mainFrame(wx.Frame):
	global MAIN_WINDOW_SIZE
	global ICON_PATH
	global MAIN_BG_COLOR
	global ALLMSG
	#global SEND_MSG
	global NAME
	global TCP_Sock

	def __init__(self, parent, id):
		wx.Frame.__init__(self, parent, id, 'fengx', size=[400,900],style=wx.DEFAULT_FRAME_STYLE)
		#---------------main Window settings----->>>>
		self.SetBackgroundColour(MAIN_BG_COLOR)
		self.CreateStatusBar()
		self.SetStatusText("fengxEngine")
		#--------------main Part of window------->>>>
		self.P_main=wx.Panel(self)
		#self.P_bot=wx.Panel(self)
		self.b_send = wx.Button(self.P_main, -1, label=u'send')
		self.b_connect = wx.Button(self.P_main, -1, label=u'connect')
		self.t_input=wx.TextCtrl(self.P_main, -1,
					" ",
				   size=(200, 100), style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)
		self.t_output=wx.TextCtrl(self.P_main, -1,
					" ",
				   size=(200, 100), style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)


		self.Bind(wx.EVT_BUTTON, self.sendMSG, self.b_send)
		self.Bind(wx.EVT_BUTTON, self.connect, self.b_connect)
		self.boxu = wx.BoxSizer(wx.VERTICAL)
		self.boxd = wx.BoxSizer(wx.HORIZONTAL)
		self.boxu.Add(self.t_output, 6, wx.EXPAND|wx.ALL ,border=2)
		self.boxu.Add(self.t_input, 2, wx.EXPAND|wx.ALL ,border=2)
		
		self.boxd.Add(self.b_connect, 1, wx.EXPAND|wx.ALL ,border=2)
		self.boxd.Add(self.b_send, 1, wx.EXPAND|wx.ALL ,border=2)
		#self.box.Add(self.resManager, 1, wx.EXPAND|wx.ALL ,border=1)
		#self.box.Add(self.dir3, 1, wx.EXPAND|wx.ALL ,border=1)
		
		self.mainBox=wx.BoxSizer(wx.VERTICAL)
		self.mainBox.Add(self.boxu,12,wx.EXPAND|wx.ALL ,border=1)
		self.mainBox.Add(self.boxd,1,wx.EXPAND|wx.ALL ,border=1)
		self.P_main.SetSizer(self.mainBox)
		self.mainBox.Fit(self.P_main)
		self.Fit()

	def sendMSG(self, evt):
		SEND_MSG=self.t_input.GetValue()
		sendStr=NAME+":>>  "+SEND_MSG+"\n"
		self.t_output.WriteText(sendStr)
		#s.send(sendStr)
		s.send(SEND_MSG)

	def connect(self,evt):
		s.connect((HOST,PORT))
		data=s.recv(4096)
		if not data: 
			print "connected fath!"
		else:
			if data=="connected success!":
				print data 

ex = wx.App()
mainF=mainFrame(parent=None, id=-1)
mainF.Show()
mainF.SetBackgroundColour(MAIN_BG_COLOR)
ex.MainLoop() 	
s.close()
