import serial
import serial.tools.list_ports

class customSerial():

    portList = None
    baudRateList = ["9600", "19200", "38400", "57600", "115200"]
    serialConnect = False
    
    def __init__(self):
        self.serialDevice = serial.Serial()
        self.portList = serial.tools.list_ports.comports()

    def connect(self,port, baudrate):
        self.serialDevice.port = port
        self.serialDevice.baudrate = baudrate

        try:
            self.serialDevice.open()
        except serial.serialutil.SerialException:
            print("port not available: ", self.serialDevice.port)

    def disconnect(self):
        self.serialDevice.close()
