from lcdui.devices import Generic, CrystalFontz
from lcdui.ui import frame
from lcdui.ui import ui
from lcdui.ui import widget
import time

#device = Generic.MockCharacterDisplay(rows=4, cols=40)
#device = CrystalFontz.CFA635Display(port='/dev/ttyUSB0')

device = Generic.MockCharacterDisplay(rows=2, cols=15)
device = CrystalFontz.CFA533Display(port='/dev/ttyUSB0')

device.ClearScreen()
device.BacklightEnable(True)

ui = ui.LcdUi(device)

f = ui.FrameFactory(frame.Frame)

line1 = f.BuildWidget(widget.LineWidget, row=0, col=0)
line1.set_contents("Hello, world!")
time.sleep(5)
line2 = f.BuildWidget(widget.LineWidget, row=1, col=10, span=6)
line2.set_contents("cutoffXXX")
time.sleep(5)
ui.PushFrame(f)
ui.Repaint()
time.sleep(5)
f = ui.FrameFactory(frame.MenuFrame)
time.sleep(5)
f.setTitle('example menu')
time.sleep(5)
f.addItem(1, 'first choice')
time.sleep(5)
f.addItem(2, 'second choice')
time.sleep(5)
f.addItem(3, 'another choice')
time.sleep(5)
f.addItem(4, 'last choice')
time.sleep(5)
ui.PushFrame(f)
time.sleep(5)
ui.Repaint()
time.sleep(5)

for i in xrange(6):
  f.scrollDown()
  ui.Repaint()
  time.sleep(0.2)

for i in xrange(6):
  f.scrollUp()
  ui.Repaint()
  time.sleep(0.2)

f = ui.FrameFactory(frame.MultiFrame)

f1 = ui.FrameFactory(frame.Frame)
line1 = f1.BuildWidget(widget.LineWidget, row=0, col=0, contents="Page 1")

f2 = ui.FrameFactory(frame.Frame)
line2 = f2.BuildWidget(widget.LineWidget, row=0, col=0, contents="Page 2")

f.AddFrame(f1, 5)
f.AddFrame(f2, 2)

ui.PushFrame(f)

for i in xrange(15):
  ui.Repaint()
  time.sleep(1)

# ui.MainLoop()

