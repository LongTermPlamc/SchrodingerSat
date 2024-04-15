from tkinter import ttk
import tkinter as tk
import time
from PIL import Image, ImageTk
from individualTkModules.SerialPanel import SerialPanel
import backend
import serial

import SerialComponent

class AppPanel():

    back = backend.Backend()
    ## Dataset para hacer store de todos los datos
    
    def __init__(self,master):
        self.master = master
        self.master.title("SchrodingerSat")

        self.frame = tk.Frame(self.master, padx= 20, pady=20)
        self.frame.grid(row=0,column=0,sticky="nsew")
        

        self.controlPanel = tk.Frame(self.frame, highlightbackground="blue", highlightthickness=2)
        self.controlPanel.grid(row=0,column = 0,sticky="nsew")

        self.connectionPanel = tk.Frame(self.controlPanel)
        self.connectionPanel.grid(row=0,column=0,sticky="nsew")
        self.connectionPanelName = tk.Label(self.connectionPanel, text="Serial Connection Panel")
        self.connectionPanelName.grid(row=0,column=0,sticky="nsew")
        self.comPortSelector = ttk.Combobox(self.connectionPanel,state="readonly", values=self.back.availablePorts)
        self.comPortSelector.current(4)
        self.comPortSelector.grid(row=1,column=0,sticky="nsew")
        self.comBaudSelector = ttk.Combobox(self.connectionPanel, state="readonly",values=self.back.availableBauds)
        self.comBaudSelector.current(0)
        self.comBaudSelector.grid(row=2,column=0,sticky="nsew")
        self.comButtonPanel = tk.Frame(self.connectionPanel)
        self.comButtonPanel.grid(row=3,column=0,sticky="nsew")
        self.connectButton = tk.Button(self.comButtonPanel, text="Connect",command=self.connect, fg="black", state = tk.NORMAL)
        self.connectButton.grid(row=0,column=0,sticky="nsew")
        self.disconnectButton = tk.Button(self.comButtonPanel, text="Disconnect",command=self.disconnect, fg="black", state=tk.DISABLED)
        self.disconnectButton.grid(row=0,column=1,sticky="nsew")

        """self.timePanel = tk.Frame(self.controlPanel)
        self.timePanel.grid(row=1, column =0,sticky="nsew")
        self.timePanelName = tk.Label(self.timePanel, text="Timing")
        self.timePanelName.grid(row=0,column=0,sticky="nsew")
        self.mainClock = tk.Label(self.timePanel, text="00:00:00", font=("Helvetica", 48))
        self.mainClock.grid(row =1, column=0,sticky="nsew")
        self.connectionClock = tk.Label(self.timePanel, text="00:00:00", font=("Helvetica", 48))
        self.connectionClock.grid(row =2, column=0,sticky="nsew")
        self.timeRefresh()"""


        self.trialPanel = tk.Frame(self.controlPanel)
        self.trialPanel.grid(row=2, column= 0,sticky="nsew")
        self.trialPanelName = tk.Label(self.trialPanel, text="Trial Panel")
        self.trialPanelName.grid(row=0,column=0,sticky="nsew")
        self.startStopFrame = tk.Frame(self.trialPanel)
        self.startStopFrame.grid(row=1,column=0,sticky="nsew")
        self.startButton = tk.Button(self.startStopFrame, text="Start", command=self.startReading, fg="black", state = tk.DISABLED)
        self.startButton.grid(row=0,column=0,sticky="nsew")
        self.stopButton = tk.Button(self.startStopFrame, text="Stop", command=self.stopReading, fg="black",state = tk.DISABLED)
        self.stopButton.grid(row=0,column=1,sticky="nsew")
        self.saveButton = tk.Button(self.trialPanel, text="Save Data",command=self.saveData, fg="black",state = tk.DISABLED)
        self.saveButton.grid(row=2,column=0,sticky="nsew")

        """self.positionImage = Image.open(".\\pythonFiles\\wildcardImage.png").resize((780,300))
        self.positionImage = ImageTk.PhotoImage(self.positionImage)
        self.velocityImage = Image.open(".\\pythonFiles\\wildcardImage.png").resize((780,300))
        self.velocityImage = ImageTk.PhotoImage(self.velocityImage)
        self.accelerationImage =Image.open(".\\pythonFiles\\wildcardImage.png").resize((780,300))
        self.accelerationImage =ImageTk.PhotoImage(self.accelerationImage)

        self.motionVarPanel = tk.Frame(self.frame,padx=5,pady=5, highlightbackground="blue", highlightthickness=2)
        self.motionVarPanel.grid(row=0,column=1,sticky="nsew")
        self.motionVarPanelName = tk.Label(self.motionVarPanel, text="Motion Variables")
        self.motionVarPanelName.grid(row=0,column=0,sticky="nsew")
        self.plotFrame = tk.Frame(self.motionVarPanel)
        self.plotFrame.grid(row=1,column=0,sticky="nsew")
        self.positionPlot = tk.Label(self.plotFrame, image=self.positionImage)
        self.positionPlot.grid(row=0, column=0,sticky="nsew")
        self.velocityPlot = tk.Label(self.plotFrame, image=self.velocityImage)
        self.velocityPlot.grid(row=1, column=0,sticky="nsew")
        self.accelerationPlot = tk.Label(self.plotFrame, image=self.accelerationImage)
        self.accelerationPlot.grid(row=2, column=0,sticky="nsew")

        self.gyroAndTermoPanel = tk.Frame(self.frame,padx=5,pady=5, highlightbackground="blue", highlightthickness=2)
        self.gyroAndTermoPanel.grid(row=0,column =2,sticky="nsew")

        self.gyroscopeImage =Image.open(".\\pythonFiles\\wildcardImage.png").resize((620,300))
        self.gyroscopeImage =ImageTk.PhotoImage(self.gyroscopeImage)

        self.gyroPanel = tk.Frame(self.gyroAndTermoPanel)
        self.gyroPanel.grid(row=0, column=0,sticky="nsew")
        self.gyroPanelName = tk.Label(self.gyroPanel,text="Gyroscope Data")
        self.gyroPanelName.grid(row=0,column=0,sticky="nsew")
        self.gyroPlot = tk.Label(self.gyroPanel, image=self.gyroscopeImage)
        self.gyroPlot.grid(row=1, column=0,sticky="nsew")

        self.temperatureImage =Image.open(".\\pythonFiles\\wildcardImage.png").resize((620,300))
        self.temperatureImage =ImageTk.PhotoImage(self.temperatureImage)
        self.pressureImage =Image.open(".\\pythonFiles\\wildcardImage.png").resize((620,300))
        self.pressureImage =ImageTk.PhotoImage(self.pressureImage)

        self.termoPanel =tk.Frame(self.gyroAndTermoPanel)
        self.termoPanel.grid(row=1,column=0,sticky="nsew") 
        self.termoPanelName = tk.Label(self.termoPanel,text="Pressure and Temperature")
        self.termoPanelName.grid(row=0,column=0,sticky="nsew")
        self.termoPlotFrame = tk.Frame(self.termoPanel)
        self.termoPlotFrame.grid(row=1, column=0,sticky="nsew")
        self.temperaturePlot = tk.Label(self.termoPlotFrame, image=self.temperatureImage)
        self.temperaturePlot.grid(row=0, column=0,sticky="nsew")
        self.pressurePlot = tk.Label(self.termoPlotFrame, image=self.pressureImage)
        self.pressurePlot.grid(row=1, column=0,sticky="nsew")"""

        

    """ def __init__(self, master):
        self.master = master
        self.master.title("SchrodingerSat")

        self.frame = tk.Frame(self.master, padx=20, pady=20)
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.columnone = tk.Frame(self.frame, padx=0, pady=0)
        self.columnone.grid(row=0, column =0, padx = 0, pady=0)

        ## Serial connection panel
        zone1 = tk.Frame(self.columnone, bg="lightblue", width=180, height=180)
        zone1.grid(row=0, column=0, padx=0, pady=5, sticky="nw")

        self.serialConnect = False
        panelName = tk.Label(zone1, text="Serial Connection Panel")
        panelName.grid(row=0, column=0, pady=(5, 10))

        comSelect = ttk.Combobox(zone1, values=[1, 2, 3, 4], width=57)
        comSelect.grid(row=1, column=0, padx=10, pady=2)

        baudSelect = ttk.Combobox(zone1, values=[1, 2, 3, 4], width=57)
        baudSelect.grid(row=2, column=0, padx=10, pady=2)

        self.connectTimeStart = 0
        zone11 = tk.Frame(zone1, bg="lightblue", width=100, height=100)
        zone11.grid(row=3, column=0, padx=10, pady=5)
        self.connectButton = tk.Button(zone11, text="Connect", fg="black", command=self.connect)
        self.connectButton.grid(row=0, column=0, padx=5)
        self.disconnectButton = tk.Button(zone11, text="Disconnect", fg="black", command=self.disconnect, state=tk.DISABLED)
        self.disconnectButton.grid(row=0, column=1, padx=5)

        ## Clock panel
        zone2 = tk.Frame(self.columnone, bg="lightblue", width=180, height=250)
        zone2.grid(row=1, column=0, padx=5, pady=5, sticky="nw")

        clockName = tk.Label(zone2, text="Clock Panel")
        clockName.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        self.globalTime = tk.Label(zone2, text="", font=("Helvetica", 48))
        self.globalTime.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.connectionTime = tk.Label(zone2, text="00:00:00", font=("Helvetica", 48))
        self.connectionTime.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.timeRefresh()

        ## Start-Stop-Save panel
        zone3 = tk.Frame(self.columnone, bg="lightblue", width=120, height=250)
        zone3.grid(row=2, column=0, padx=5, pady=5, sticky="nw")

        trialName = tk.Label(zone3, text="Trial Panel")
        trialName.grid(row=0, column=0, pady=(5, 10))

        zone31 = tk.Frame(zone3, bg="lightblue", width=10, height=100)
        zone31.grid(row=1, column=0, padx=10, pady=5)
        self.startButton = tk.Button(zone31, text="Start", fg="black", width=22, command=self.startMeasure)
        self.startButton.grid(row=0, column=0, padx=5)
        self.stopButton = tk.Button(zone31, text="Stop", fg="black", width=22, command=self.stopMeasure)
        self.stopButton.grid(row=0, column=1, padx=5)

        zone32 = tk.Frame(zone3, bg="lightblue", width=10, height=100)
        zone32.grid(row=2, column=0, padx=5, pady=5)
        self.saveButton = tk.Button(zone32, text="Save Data", fg="black", width=47, command=self.saveData)
        self.saveButton.grid(row=0, column=0, padx=0, pady=0)

        self.columntwo = tk.Frame(self.frame, padx=0, pady=0)
        self.columntwo.grid(row=0, column =1, padx = 0, pady=0)"""

    """ def __init__(self, master):
        self.master = master
        self.master.title("SchrodingerSat")

        self.frame = tk.Frame(self.master, padx=20, pady=20)
        self.frame.pack(expand=True,fill="both")

        #zone1 = tk.Frame(self.frame, bg="lightblue", width=180, height=180)
        #zone1.grid(row=0, column=0, padx=5, pady=5, sticky="nw")

        ##Serial conection panel
        zone1 = tk.Frame(self.frame, bg="lightblue",width=180,height=180)
        zone1.pack(expand=False, anchor="nw", fill="none", padx=5, pady = 5)

        self.serialConnect = False
        panelName = tk.Label(zone1, text="Serial Connection Panel")
        panelName.pack(anchor="nw",padx = 10, pady=5, ipady=5)
        comSelect = ttk.Combobox(zone1,values =[1,2,3,4],width=60)
        comSelect.pack(side="top",anchor="w", pady=2, padx=10, ipadx=5)
        baudSelect = tk.Entry(zone1,width=63)
        baudSelect.pack(side="top",anchor="w",pady=2, padx=10, ipadx=5)

        self.connectTimeStart = 0
        zone11 = tk.Frame(zone1,bg = "lightblue",width=100,height=100)
        zone11.pack(side="left", padx=10, pady=5)
        self.connectButton = tk.Button(zone11,text="Connect",fg="black",command=self.connect)
        self.connectButton.pack(side="left",padx=5,ipadx=10)
        self.disconnectButton = tk.Button(zone11,text="Disconnect",fg="black",command=self.disconnect, state=tk.DISABLED)
        self.disconnectButton.pack(side="left",padx =5,ipadx=10)

        ##Clock panel
        zone2 = tk.Frame(self.frame, bg="lightblue",width=180,height=250)
        zone2.pack(expand=False, anchor="nw", fill="none", padx=5, pady = 5)

        clockName = tk.Label(zone2, text="Clock Panel")
        clockName.pack(anchor="nw",padx = 10, pady=5, ipady=5)
        self.globalTime = tk.Label(zone2, text="",font=("Helvetica",48))
        self.globalTime.pack(side= "top",anchor="w",padx=10,pady=5, ipadx=5)
        self.connectionTime = tk.Label(zone2, text="00:00:00",font=("Helvetica",48))
        self.connectionTime.pack(side= "top",anchor="w",padx=10,pady=5, ipadx=5)
        self.timeRefresh()

        ##Start-Stop-Save panel
        zone3 = tk.Frame(self.frame, bg="lightblue",width=120,height=250)
        zone3.pack(expand=False, anchor="nw", fill="none", padx=5, pady = 5)

        trialName = tk.Label(zone3, text="Trial Panel")
        trialName.pack(anchor="nw",padx = 10, pady=5, ipady=5)

        zone31 = tk.Frame(zone3,bg = "lightblue",width=10,height=100)
        zone31.pack(side="top", padx=10, pady=5)
        self.startButton = tk.Button(zone31,text="Start",fg="black",width=22,command=self.startMeasure)
        self.startButton.pack(side="left",padx=5,ipadx=0, pady=0, ipady=0)
        self.stopButton = tk.Button(zone31,text="Stop",fg="black",width=22,command=self.stopMeasure)
        self.stopButton.pack(side="right",padx=5,ipadx=0,pady=0, ipady=0)

        zone32 = tk.Frame(zone3,bg = "lightblue",width=10,height=100)
        zone32.pack(side="bottom", padx=5, pady=5)
        self.saveButton = tk.Button(zone32,text="Save Data",fg="black",width=47,command=self.saveData)
        self.saveButton.pack(side="bottom",padx=0,ipadx=0, pady=0, ipady=0) """
        
    """def createSerialPanel(self,parent):
        SerialPanel(parent)"""


    def connect(self):
        port = self.comPortSelector.get()
        baud = int(self.comBaudSelector.get()) if type(self.comBaudSelector.get()) != int else self.comBaudSelector.get()

        self.back.serialConnect(port,baud,self.connectButton,self.disconnectButton)

        self.startButton.config(state=tk.NORMAL)
        #self.stopButton.config(state=tk.NORMAL)
        #self.saveButton.config(state=tk.NORMAL)
        
    def disconnect(self):
        self.back.serialDisconnect(self.connectButton,self.disconnectButton)
        self.startButton.config(state=tk.DISABLED)
        self.stopButton.config(state=tk.DISABLED)
        self.saveButton.config(state=tk.DISABLED)

    def startReading(self):
        self.back.readActive = True
        print(f"Serial lecture started")
        self.back.initDatabase()
        self.stopButton.config(state=tk.NORMAL)
        self.startButton.config(state=tk.DISABLED)
        self.master.after(10, self.readAndWrite)


    def readAndWrite(self):
        self.back.serialReadline()
        self.back.updateDB()
        self.master.after(1000, self.readAndWrite)

    
    def stopReading(self):
        self.back.readActive = False
        self.back.dataBuffer = None
        print(f"Serial lecture stopped")
        self.startButton.config(state=tk.NORMAL)
        self.stopButton.config(state=tk.DISABLED)
        self.saveButton.config(state=tk.NORMAL)

    def saveData(self):
        self.back.saveData()
        self.saveButton.config(state=tk.DISABLED)



    """def format_seconds(self, fullseconds):
        hours, remainder = divmod(fullseconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def timeRefresh(self):
        currentTime = time.strftime('%H:%M:%S')
        self.mainClock.config(text = currentTime)

        if self.serialConnect:
            connectionTime = int(time.time() - self.connectTimeStart)
            formattedTime = self.format_seconds(connectionTime)
            self.connectionClock.config(text = formattedTime)
        else:
            self.connectionClock.config(text = "00:00:00")
        
        self.master.after(1000, self.timeRefresh)

    def startMeasure(self):
        return 0
    
    def stopMeasure(self):
        return 0
    
    def saveData(self):
        return 0"""

def main():
    root = tk.Tk()
    root.geometry("1920x1080")
    app = AppPanel(root)
    root.resizable(True,True)
    root.mainloop()

if __name__ == "__main__":
    main()