import wx
 
class MyFrame(wx.Frame):
    def __init__(self, parent=None, id=-1, title=None):
        wx.Frame.__init__(self, parent, id, title, size=(380,400))
        self.statbmp = wx.StaticBitmap(self)
        self.draw_image()
        self.save_image()
 
    def draw_image(self):
        # select the width and height of the blank bitmap
        # should fit the client frame
        w, h = 340, 340
        # create the blank bitmap as a draw background
        draw_bmp = wx.EmptyBitmap(w, h)
        # create the canvas on top of the draw_bmp
        canvas_dc = wx.MemoryDC(draw_bmp)
        # fill the canvas white
        canvas_dc.SetBrush(wx.Brush('white'))
        canvas_dc.Clear()
 
        # draw a bunch of circles ...
        # pen colour
        canvas_dc.SetPen(wx.Pen('red', 1))
        # fill colour
        canvas_dc.SetBrush(wx.Brush('yellow'))
        for x in range(10, 180, 10):
            y = x
            r = x
            canvas_dc.DrawCircle(x, y, r)
 
        # now put the canvas drawing into a bitmap to display it
        # remember the canvas is on top of the draw_bmp
        self.statbmp.SetBitmap(draw_bmp)
 
    def save_image(self):
        """save the drawing"""
        finished_image = self.statbmp.GetBitmap()
        #finished_image.SaveFile("mydrawing.png", wx.BITMAP_TYPE_PNG)
        finished_image.SaveFile("mydrawing.jpg", wx.BITMAP_TYPE_JPEG)
 
 
app = wx.App(0)
MyFrame(title='canvas draw and save').Show()
app.MainLoop()