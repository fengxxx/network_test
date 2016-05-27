import wx
from _globalData import *
from socket_client import chatClient

class mainFrame ( wx.Frame ):
    lastPos=[0,0]
    canMove=False
    canSize=False
    mousePos=[0,0]
    pos=[400,300]
    size=[0,0]
    isMaxWindow=False
    lastWindowSize=(0,0)
    lastWindowPos=(0,0)
    #print "sss"
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"FengxEngine 1.0", pos = wx.DefaultPosition, size = wx.Size( 876,685 ), style =wx.DEFAULT_FRAME_STYLE  ) #wx.NO_BORDER|wx.TAB_TRAVERSAL ) #wx.RESIZE_BORDER|

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetForegroundColour( UI_COLOR_MAIN_FG )
        self.SetBackgroundColour( UI_COLOR_MAIN_BG )
        # self.statusBar_main = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
        # self.statusBar_main.SetBackgroundColour((66,66,66))# wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )


        #--------------Menu
        # ID_NEW_SCENE = 1000
        # ID_IMPORT_FILE = 1001
        # ID_EXIT = 1002
        # self.m_menubar1 = wx.MenuBar( 0 )
        # self.m_menubar1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
        # self.m_menubar1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

        # self.file = wx.Menu()
        # self.newScene = wx.MenuItem( self.file, ID_NEW_SCENE, u"New Scene", wx.EmptyString, wx.ITEM_NORMAL )
        # self.file.AppendItem( self.newScene )

        # self.importFile = wx.MenuItem( self.file, ID_IMPORT_FILE, u"Import File", wx.EmptyString, wx.ITEM_NORMAL )
        # self.file.AppendItem( self.importFile )

        # self.exit = wx.MenuItem( self.file, ID_EXIT, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
        # self.file.AppendItem( self.exit )

        # self.m_menubar1.Append( self.file, u"File" )

        #self.SetMenuBar( self.m_menubar1 )
        #--------------Menu

        Sizer_main_V = wx.BoxSizer( wx.VERTICAL )

        bSizer_mainScene = wx.BoxSizer( wx.HORIZONTAL )

        #self.p_scenes = wx.Panel( self)#, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        #self.p_scenes.SetMinSize( wx.Size( 100,100 ) )

        # self.sceneWindow=mainGlCanvas(self)
        # self.sceneWindow.SetMinSize( wx.Size( 300,100 ) )
        #
        # bSizer_mainScene.Add( self.sceneWindow, 4, wx.ALL|wx.EXPAND, 0 )
        #
        # self.tree_project=sceneTreePanel(self, wx.NewId(), (0,0) , (100,100),
        #                         wx.TR_HAS_BUTTONS
        #                         |wx.TR_HAS_VARIABLE_ROW_HEIGHT
        #                         |wx.TR_TWIST_BUTTONS
        #                         |wx.TR_SINGLE
        #                         |wx.TR_MULTIPLE
        #                         |wx.TR_NO_LINES
        #                         |wx.TR_FULL_ROW_HIGHLIGHT
        #                         |wx.TR_EDIT_LABELS
        #                         |wx.TR_EXTENDED
        #
        #                         #wx.TR_HIDE_ROOT
        #                         #|wx.TR_NO_BUTTONS
        #                        )

        # self.tree_project = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
        # self.tree_project.SetForegroundColour(UI_COLOR_sceneTree_FG )
        # self.tree_project.SetBackgroundColour(UI_COLOR_sceneTree_BG)
        # self.tree_project.SetHelpText( u"fengx" )
        # self.tree_project.SetMinSize( wx.Size( 200,300 ) )
        # self.tree_project.SetMaxSize( wx.Size( 350,-1 ) )
        #
        #
        #
        # log=""
        # dt = MyFileDropTarget(self.sceneWindow, log)
        # self.SetDropTarget( dt )
        #


        self.p_moveBar = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.p_moveBar.SetBackgroundColour( UI_COLOR_movebar_BG )
        self.p_moveBar.SetMinSize( wx.Size( 100,25 ) )
        self.p_moveBar.SetMaxSize( wx.Size( -1,25 ) )
        #self.title=wx.StaticText(parent=self.p_moveBar,-1,"xx")
        self.title=wx.StaticText(self.p_moveBar, -1, "VisualFengx_1.0")
        self.title.SetBackgroundColour(UI_COLOR_movebar_BG )
        self.title.SetForegroundColour(UI_COLOR_movebar_FG )


        b_close_bmp=wx.Bitmap("b_max.bmp",wx.BITMAP_TYPE_BMP)
        mask = wx.Mask(b_close_bmp, wx.BLUE)
        b_close_bmp.SetMask(mask)

        b_max_bmp=wx.Bitmap("b_max.bmp",wx.BITMAP_TYPE_BMP)
        mask = wx.Mask(b_max_bmp, wx.BLUE)
        b_max_bmp.SetMask(mask)

        b_min_bmp=wx.Bitmap("b_max.bmp",wx.BITMAP_TYPE_BMP)
        mask = wx.Mask(b_min_bmp, wx.BLUE)
        b_min_bmp.SetMask(mask)



        self.b_close= wx.BitmapButton(self.p_moveBar, -1, b_close_bmp, style = wx.NO_BORDER)
        self.b_close.SetBackgroundColour(UI_COLOR_movebar_BG )
        self.b_close.Bind(wx.EVT_BUTTON, self.close)

        self.b_max= wx.BitmapButton(self.p_moveBar, -1, b_max_bmp, style = wx.NO_BORDER)
        self.b_max.SetBackgroundColour(UI_COLOR_movebar_BG )
        self.b_max.Bind(wx.EVT_BUTTON, self.maxWindow)

        self.b_min= wx.BitmapButton(self.p_moveBar, -1, b_min_bmp, style = wx.NO_BORDER)
        self.b_min.SetBackgroundColour(UI_COLOR_movebar_BG )
        self.b_min.Bind(wx.EVT_BUTTON, self.minWindow)

        self.sizebar = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.sizebar.SetMinSize( wx.Size( 100,15 ) )
        self.sizebar.SetMaxSize( wx.Size( -1,15 ) )
        self.sizebar.SetBackgroundColour( UI_COLOR_sizebar_BG )


        self.p_mainTool = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.p_mainTool.SetMinSize( wx.Size( 100,5 ) )
        self.p_mainTool.SetMaxSize( wx.Size( -1,5 ) )
        self.p_mainTool.SetBackgroundColour(UI_COLOR_mainToolbar_BG)


        self.box_movebar = wx.BoxSizer( wx.HORIZONTAL )
        self.box_movebar.AddSpacer( ( 0, 0), 1, wx.EXPAND, 0 )
        self.box_movebar.Add( self.title, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )
        self.box_movebar.AddSpacer( ( 0, 0), 1, wx.EXPAND, 0 )
        self.box_movebar.Add( self.b_min, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )
        self.box_movebar.Add( self.b_max, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )
        self.box_movebar.Add( self.b_close, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )


        self.p_moveBar.SetSizer( self.box_movebar )
        self.p_moveBar.Layout()
        self.box_movebar.Fit( self.p_moveBar)



        Sizer_main_V.Add( self.p_moveBar, 1, wx.EXPAND |wx.ALL, 0 )
        Sizer_main_V.Add( self.p_mainTool, 1, wx.EXPAND |wx.ALL, 0 )


        # bSizer_mainScene.Add( self.tree_project, 1, wx.ALL|wx.EXPAND, 0 )


        # Sizer_main_V.Add( bSizer_mainScene, 7, wx.EXPAND, 0 )
        Sizer_main_V.Add( self.sizebar, 1, wx.EXPAND, 0 )



        self.SetSizer( Sizer_main_V )
        self.Layout()

        self.Centre( wx.BOTH )

        self.p_moveBar.Bind(wx.EVT_LEFT_UP, self.OnMouseLeftUp)
        self.p_moveBar.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLeftDown)
        self.p_moveBar.Bind(wx.EVT_MOTION,  self.OnMove)
        self.p_moveBar.Bind(wx.EVT_RIGHT_UP,  self.popupmenu)
        self.p_moveBar.Bind(wx.EVT_LEFT_DCLICK,  self.maxWindow)

        #self.title.Bind(wx.EVT_LEFT_UP, self.OnMouseLeftUp)
        #self.title.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLeftDown)
        #self.title.Bind(wx.EVT_MOTION,  self.OnMove)
        self.title.Bind(wx.EVT_RIGHT_UP,  self.popupmenu)

        # self.p_moveBar.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBackGroundm)
        #self.p_mainTool.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBackGround)
        #self.tree_project.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBackGround)
        #self.statusBar_main.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBackGround)
        #self.bg=wx.StaticBitmap(self.p_moveBar,-1,  bmp, (0,0))
        #self.bga=wx.Button(self.p_moveBar,-1)
        self.Bind(wx.EVT_UPDATE_UI,self.upDate)

        self.sizebar.Bind(wx.EVT_LEFT_UP, self.OnSizeMouseLeftUp)
        self.sizebar.Bind(wx.EVT_LEFT_DOWN, self.OnSizeMouseLeftDown)
        self.sizebar.Bind(wx.EVT_MOTION,  self.OnSizeMove)


    def popupmenu(self,event):
        self.ppmenu = wx.Menu()
        pyc=wx.NewId()
        self.newScene = wx.MenuItem( self.ppmenu, pyc, u"Console", wx.EmptyString, wx.ITEM_NORMAL )
        self.ppmenu.AppendItem( self.newScene )
        #self.ppmenu.AppendItem( self.newScene )
        self.Bind(wx.EVT_MENU, self.createPyConsole, id=pyc)
        self.PopupMenu(self.ppmenu)
        self.ppmenu.Destroy()

    def minWindow(self,event):
            self.Show(False)
    def maxWindow(self,event):
        if self.isMaxWindow:
            self.isMaxWindow=False
            #self.SetSize(self.lastWindowSize)
            #self.SetPosition(self.lastWindowPos)
            self.ShowFullScreen(False)
        else:
            self.lastWindowSize=self.GetClientSize()
            self.lastWindowPos=self.GetPositionTuple()
            #self.SetSize(wx.GetDisplaySize())
            self.ShowFullScreen(True)
            #self.SetPosition((0,0))
            self.isMaxWindow=True
    def close(self,event):
            sys.exit()
    def upDate(self,event):
        ()
        #self.SetStatusText(("FPS:  "+str(self.sceneWindow.FPS)))
    def __del__( self ):
        pass

    def OnMove(self, event):
        newPosX=event.GetPosition()[0]-self.lastPos[0]+self.pos[0]
        newPosY=event.GetPosition()[1]-self.lastPos[1]+self.pos[1]
        newPos=wx.Point=(newPosX,newPosY)
        self.mousePos[0]=event.GetPosition()[0]
        self.mousePos[1]=event.GetPosition()[1]
        if self.canMove:
            self.SetPosition(newPos)
            self.pos[0]=newPos[0]
            self.pos[1]=newPos[1]

    def OnMouseLeftDown(self, event):
        self.p_moveBar.SetCursor(wx.StockCursor(wx.CURSOR_HAND))
        self.p_moveBar.CaptureMouse()
        self.lastPos[0]=event.GetPosition()[0]
        self.lastPos[1]=event.GetPosition()[1]
        self.canMove=True

    def OnMouseLeftUp(self, event):
        self.p_moveBar.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
        if self.p_moveBar.HasCapture():
            self.p_moveBar.ReleaseMouse()
        self.canMove=False

    def OnEraseBackGround(self,event):
        dc=event.GetDC()
        if not dc:
            dc=wx.ClientDC(self)
            rect=self.GetUpdateRegion().Getbox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp=wx.Bitmap("MAIN_BG_IMAGE.bmp")
        bmp_movebar=wx.Bitmap("MAIN_MOVEBAR_IMAGE.bmp")
        #dc.DrawBitmap(bmp,0,0)
        self.TileBackground(dc,bmp)
    def OnEraseBackGroundm(self,event):
        dc=event.GetDC()
        if not dc:
            dc=wx.ClientDC(self)
            rect=self.GetUpdateRegion().Getbox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp=wx.Bitmap("MAIN_BG_IMAGE.bmp")
        bmp_movebar=wx.Bitmap("MAIN_MOVEBAR_IMAGE.bmp")
        #dc.DrawBitmap(bmp,0,0)
        self.TileBackground(dc,bmp_movebar)



    def TileBackground(self, dc,bmp):
            sz = self.GetClientSize()
            w = bmp.GetWidth()
            h = bmp.GetHeight()

            x = 0

            while x < sz.width:
                y = 0

                while y < sz.height:
                    dc.DrawBitmap(bmp, x, y)
                    y = y + h

                x = x + w


    # def OnSizeMove(self, event):
    #     self.sizebar.SetCursor(wx.StockCursor(wx.CURSOR_SIZENWSE))
    #     newSizeX=wx.GetMousePosition()[0]-self.lastPos[0]+self.GetClientSize()[0]
    #     newSizeY=wx.GetMousePosition()[1]-self.lastPos[1]+self.GetClientSize()[1]
    #     newSize=wx.Point=(newSizeX,newSizeY)
    #     if self.canSize:
    #         self.SetSize(newSize)
    #     self.lastPos[0]=wx.GetMousePosition()[0]
    #     self.lastPos[1]=wx.GetMousePosition()[1]
    def OnSizeMove(self,event):
        newSizeX=int(wx.GetMousePosition()[0]-self.lastPos[0]+self.GetClientSize()[0])
        newSizeY=int(wx.GetMousePosition()[1]-self.lastPos[1]+self.GetClientSize()[1])
        newSize=(newSizeX,newSizeY)
        if self.canSize:
            self.SetSize(newSize)
        self.lastPos=wx.GetMousePosition()
        self.SetCursor(wx.StockCursor(wx.CURSOR_SIZENWSE))

    def OnSizeMouseLeftDown(self, event):
        self.sizebar.CaptureMouse()
        self.lastPos=wx.GetMousePosition()
        self.canSize=True

    def OnSizeMouseLeftUp(self, event):
        self.p_moveBar.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
        if self.sizebar.HasCapture():
            self.sizebar.ReleaseMouse()
        self.canSize=False
    def createPyConsole(self,event):
        console=PyConsoleFrame(parent=None,id=-1)
        console.Show()

class mainWindow ( wx.Frame ):
    lastPos=[0,0]
    canMove=False
    canSize=False
    mousePos=[0,0]
    pos=[400,300]
    size=[0,0]
    isMaxWindow=False
    lastWindowSize=(0,0)
    lastWindowPos=(0,0)
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"FengxEngine 1.0", pos = wx.DefaultPosition, size = wx.Size( 876,685 ), style =wx.DEFAULT_FRAME_STYLE  ) #wx.NO_BORDER|wx.TAB_TRAVERSAL ) #wx.RESIZE_BORDER|

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetForegroundColour( UI_COLOR_MAIN_FG )
        self.SetBackgroundColour( UI_COLOR_MAIN_BG )

        self.tex_show = wx.TextCtrl(self, -1, "Test it out and see", size=(125, -1),style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)
        self.tex_input = wx.TextCtrl(self, -1, "input", size=(125, -1),style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)
        self.but_send = wx.Button(self, 10, "send", (20, 20))
        self.but_send.Bind(wx.EVT_BUTTON, self.OnClick_send)
        self.tex_show.SetBackgroundColour( UI_COLOR_MAIN_BG )
        self.tex_input.SetBackgroundColour( UI_COLOR_MAIN_BG )

        Sizer_main = wx.BoxSizer( wx.VERTICAL )
        Sizer_send = wx.BoxSizer( wx.HORIZONTAL )
        # self.p_moveBar.Layout()
        # self.box_movebar.Fit( self.p_moveBar)

        Sizer_send.Add( self.tex_input, 7, wx.EXPAND |wx.ALL, 0 )
        Sizer_send.Add( self.but_send, 3, wx.EXPAND |wx.ALL, 0 )
        Sizer_main.Add( self.tex_show, 6, wx.EXPAND |wx.ALL, 0 )
        Sizer_main.Add( Sizer_send, 4, wx.EXPAND |wx.ALL, 0 )
        # bSizer_mainScene.Add( self.tree_project, 1, wx.ALL|wx.EXPAND, 0 )

        self.SetSizer( Sizer_main )
        self.Layout()
        self.Centre( wx.BOTH )

    def OnClick_send(self,event):
        print self.tex_input.GetValue()

if __name__=='__main__':
    mainApp = wx.App()
    mainWindow=mainWindow(parent=None)
    mainWindow.Show()
    mainApp.MainLoop()
