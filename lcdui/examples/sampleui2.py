from lcdui.devices import Generic, CrystalFontz
from lcdui.ui import frame
from lcdui.ui import ui
from lcdui.ui import widget
import time

#device = Generic.MockCharacterDisplay(rows=4, cols=40)
#device = CrystalFontz.CFA635Display(port='/dev/ttyUSB0')

device = Generic.MockCharacterDisplay(rows=2, cols=16)
device = CrystalFontz.CFA533Display(port='/dev/ttyUSB0')

device.ClearScreen()
device.BacklightEnable(True)

# create LCD UI from USB dev
ui = ui.LcdUi(device)


###########
# Example 1
###########
f = ui.FrameFactory(frame.Frame)
line1 = f.BuildWidget(widget.LineWidget, row=0, col=0)
line2 = f.BuildWidget(widget.LineWidget, row=1, col=10, span=6)
line1.set_contents("Hello, world!")
line2.set_contents("cutoffXXX")
ui.PushFrame(f)
ui.Repaint()
"""PRINTS the following:"""
#Hello World!   #
#         cutoff#


ui.MainLoop()
#ui.StepLoop()
