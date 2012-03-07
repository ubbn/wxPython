import wx

if __name__ == "__main__":
    app = wx.PySimpleApp()
    progressMax = 100
    dialog = wx.ProgressDialog("A progress box", "Time remaining", progressMax,
            style=wx.PD_CAN_ABORT | wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME)
    keepGoing = True
    count = 0
    while keepGoing and count < progressMax:
        count = count + 1
        wx.Sleep(1)
        keepGoing = dialog.Update(count)

    dialog.Destroy()
    
