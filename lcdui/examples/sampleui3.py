from lcdui.devices import Generic, CrystalFontz
from lcdui.ui import frame
from lcdui.ui import ui
from lcdui.ui import widget
import time
import logging

logging.basicConfig(level=logging.DEBUG)

logging.info("Program started")

device = CrystalFontz.CFA533Display(port='/dev/ttyUSB0')

device.ClearScreen()
device.BacklightEnable(True)

ui = ui.LcdUi(device)

f = ui.FrameFactory(frame.Frame)


f = ui.FrameFactory(frame.MenuFrame)
f.setTitle('Press Up/Down')
f.addItem(1, 'first choice')
f.addItem(2, 'second choice')
f.addItem(3, 'another choice')
f.addItem(4, 'last choice')
ui.PushFrame(f)
ui.Repaint()

ui.MainLoop()

