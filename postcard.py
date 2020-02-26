from PIL import Image
import wx
some = []
 
class MainPanel(wx.Panel):
 
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.frame = parent
        sizer = wx.BoxSizer(wx.VERTICAL)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        label = some[0]
        btn = wx.Button(self, label=label)
        btn.Bind(wx.EVT_BUTTON, self.h0)
        sizer.Add(btn, 0, wx.ALL, 5)
        
        label = some[1]
        btn = wx.Button(self, label=label)
        btn.Bind(wx.EVT_BUTTON, self.h1)
        sizer.Add(btn, 0, wx.ALL, 5)
        
        label = some[2]
        btn = wx.Button(self, label=label)
        btn.Bind(wx.EVT_BUTTON, self.h2)
        sizer.Add(btn, 0, wx.ALL, 5)
        
        label = some[3]
        btn = wx.Button(self, label=label)
        btn.Bind(wx.EVT_BUTTON, self.h3)
        sizer.Add(btn, 0, wx.ALL, 5)
        
        label = some[4]
        btn = wx.Button(self, label=label)
        btn.Bind(wx.EVT_BUTTON, self.h4)
        sizer.Add(btn, 0, wx.ALL, 5)
        
        label = some[5]
        btn = wx.Button(self, label=label)
        btn.Bind(wx.EVT_BUTTON, self.h5)
        sizer.Add(btn, 0, wx.ALL, 5)
        
        label = some[6]
        btn = wx.Button(self, label=label)
        btn.Bind(wx.EVT_BUTTON, self.h6)
        sizer.Add(btn, 0, wx.ALL, 5)
        
        label = some[7]
        btn = wx.Button(self, label=label)
        btn.Bind(wx.EVT_BUTTON, self.h7)
        sizer.Add(btn, 0, wx.ALL, 5)
        
        label = some[8]
        btn = wx.Button(self, label=label)
        btn.Bind(wx.EVT_BUTTON, self.h8)
        sizer.Add(btn, 0, wx.ALL, 5)
        
        label = some[9]
        btn = wx.Button(self, label=label)
        btn.Bind(wx.EVT_BUTTON, self.h9)
        sizer.Add(btn, 0, wx.ALL, 5)
        
            
        hSizer.Add((1,1), 1, wx.EXPAND)
        hSizer.Add(sizer, 0, wx.TOP, 150)
        hSizer.Add((1,1), 0, wx.ALL, 0)
        
        self.SetSizer(hSizer)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
    
    def h0(self, event):
        img = Image.open(r'p1.jpg')
        img.show()
    
    def h1(self, event):
        img = Image.open(r'p2.jpg')
        img.show()
        
    def h2(self, event):
        img = Image.open(r'p3.jpg')
        img.show()
        
    def h3(self, event):
        img = Image.open(r'p4.jpg')
        img.show()
        
    def h4(self, event):
        img = Image.open(r'p5.jpg')
        img.show()
        
    def h5(self, event):
        img = Image.open(r'p6.jpg')
        img.show()
    
    def h6(self, event):
        img = Image.open(r'p7.jpg')
        img.show()
        
    def h7(self, event):
        img = Image.open(r'p8.jpg')
        img.show()
        
    def h8(self, event):
        img = Image.open(r'p9.jpg')
        img.show()
        
    def h9(self, event):
        img = Image.open(r'p10.jpg')
        img.show()
 
    def OnEraseBackground(self, evt):
        """
        Добавляем фоновое изображение.
        """
        dc = evt.GetDC()
        if not dc:
            dc = wx.ClientDC(self)

            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
 
        dc.Clear()
        bmp = wx.Bitmap("fon.jpg")
        dc.DrawBitmap(bmp, 0, 0)
 
 
class MainFrame(wx.Frame):
 
    def __init__(self):
        wx.Frame.__init__(self, None, size=(800,570))
        panel = MainPanel(self)
        self.Center()
 
 
class Main(wx.App):
 
    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self, redirect, filename)
        dlg = MainFrame()
        dlg.Show()
 
 
if __name__ == "__main__":
    app = Main()
    app.MainLoop()
