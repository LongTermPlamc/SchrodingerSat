import serial
import serial.tools.list_ports
import pandas as pd
import time
import tkinter as tk

class Backend():

    db = None
    serial = None
    availablePorts = None
    port = None
    readActive=False
    essayTime = None
    essayName = None
    dataBuffer = None


    def __init__(self):
        self.serial = serial.Serial()
        self.availablePorts = ["COM1","COM2","COM3","COM4","COM5","COM6"]
        self.availableBauds = [9600, 19200, 38400, 57600, 115200]
        #self.availablePorts  = serial.tools.list_ports.comports()

    def serialConnect(self, comboPort,comboBaud,connect,disconnect):

        print(comboPort, comboBaud)

        if not comboPort or not comboBaud:
            return
        
        self.serial.port = comboPort
        self.serial.baudrate = comboBaud
        self.serial.timeout = 0.1

        try:
            self.serial.open()
            print(f"SerialPort succesfully open at port: {self.serial.port} with baudrate: {self.serial.baudrate}.")
            connect.config(state=tk.DISABLED)
            disconnect.config(state=tk.NORMAL)
        except serial.SerialException as e:
            print("Failed to open port: ", e)


    def serialDisconnect(self,connect,disconnect):
        try:
            self.serial.close()
            print(f"SerialPort succesfully closed.")
            connect.config(state=tk.NORMAL)
            disconnect.config(state=tk.DISABLED)
        except serial.SerialException as e:
            print("Failed to close port at: ", e)
        

    def serialReadline(self):
        if self.serial.is_open and self.readActive:
            self.dataBuffer = self.serial.readline()
            self.dataBuffer= self.dataBuffer.decode().strip()
            print(self.dataBuffer)


    def updateDB(self):
        if self.dataBuffer and self.dataBuffer[0]=="(" and self.dataBuffer[-1]==")":
            cleanDataStr = self.dataBuffer.strip("()").split(",")
            cleanDataNmr = [int(i) for i in cleanDataStr]
        else:
            return
        
        if type(self.db)==pd.DataFrame and len(cleanDataNmr)==len(self.db.columns):
            self.db.loc[len(self.db)] = cleanDataNmr
            
    def serialWrite(self):
        pass

    def initDatabase(self):
        self.essayTime = time.strftime("%Y-%m-%d_%H-%M-%S")
        self.essayName = f"./SchrodingerSat_{self.essayTime}.csv"
        self.db = pd.DataFrame(columns=["time","Ax", "Ay", "Az", "Temperatura", "Presion", "Altura1", "Gx", "Gy", "Gz"])
        print(f"DB, defined with the following columns {self.db.columns} at time {self.essayTime}")
        print(self.essayName)


    def saveData(self):
        if not self.readActive:
            self.db.to_csv(self.essayName)

        print(f"Data saved to file {self.essayName}")

