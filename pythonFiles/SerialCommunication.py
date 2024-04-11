import serial
import time

class SerialCommunication:
    def __init__(self, port, baudrate):
        self.ser = serial.Serial(port, baudrate)
        time.sleep(2)

    def readdata(self):
        if self.ser.isOpen():
            # Leer datos desde el puerto serial
            data = self.ser.readline().decode('latin1').strip()
            return data
        else:
            print("Error: La comunicación serial no está abierta.")

    def __close__(self):
        if self.ser.isOpen():
            self.ser.close()
            print("Comunicación serial cerrada.")
        else:
            print("Error: La comunicación serial ya está cerrada.")