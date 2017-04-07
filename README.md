# wxPython in Action

[wxPython](http://www.wxpython.org/) is a Python extension library for developing cross platform GUI. This repostiory contains a variety of code examples for developing different GUI elements with wxPython. It is an alternative to other GUI development toolkits like PyQt, Tkinter etc.

## Usage
This simple module demonstrantes the creation of the two main objects in wxPython which are the main window object and the application object, followed by passing the control to the event-driven system by calling MainLoop() which manages the user-interactive part of the program.

```python
#!/usr/bin/env python
import wx

class App(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None, title='Bare')
        frame.Show()
        return True

app = App()
app.MainLoop()
```

## Download
Download or fork the repository

```sh
git clone git@github.com:ubbn/wxPython.git
```
or
```sh
wget https://github.com/ubbn/wxPython/archive/master.zip
```

## Support & Contributing

[Noel Rappin](https://www.amazon.com/Noel-Rappin/e/B002BLQ488) is a Senior Developer and Agile Coach at Table XI. Noel has authored multiple technical books, including "Rails 4 Test Prescriptions", "Master Space and Time With JavaScript", Trust-Driven Development and several more. If you like those example codes, I encourage you to buy the book [wxPython in Action](http://www.amazon.com/Wxpython-Action-Noel-Rappin/dp/1932394621). Contact with him on his [website](http://www.noelrappin.com/) or follow him on [twitter](https://twitter.com/noelrap).

