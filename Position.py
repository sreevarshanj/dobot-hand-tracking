import pydobot
from serial.tools import list_ports
port = "COM3"
device = pydobot.Dobot(port=port, verbose=True)
(x, y, z, r, j1, j2, j3, j4) = device.pose()
print("pose",x,y,z)
device.move_to(int(168.9253387451172), 0 ,int(49), r, wait=False)