from tkinter import ttk
import tkinter as tk
import time

class AppPanel:

    def __init__(self, master):
        self.master = master
        self.master.title("SchrodingerSat")

        self.frame = tk.Frame(self.master, padx=20, pady=20)
        self.frame.pack(expand=True,fill="both")

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
        zone3 = tk.Frame(self.frame, bg="lightblue",width=180,height=250)
        zone3.pack(expand=False, anchor="nw", fill="none", padx=5, pady = 5)
        

    def connect(self):
        self.connectButton.config(state=tk.DISABLED)
        self.disconnectButton.config(state=tk.NORMAL)
        self.serialConnect = True

        self.connectTimeStart = time.time()
        self.timeRefresh()
    
    def disconnect(self):
        self.connectButton.config(state=tk.NORMAL)
        self.disconnectButton.config(state=tk.DISABLED)
        self.serialConnect = False
        self.timeRefresh()

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def timeRefresh(self):
        currentTime = time.strftime('%H:%M:%S')
        self.globalTime.config(text = currentTime)

        if self.serialConnect:
            connectionTime = int(time.time() - self.connectTimeStart)
            formattedTime = self.format_seconds(connectionTime)
            self.connectionTime.config(text = formattedTime)
        else:
            self.connectionTime.config(text = "00:00:00")
        
        self.master.after(1000, self.timeRefresh)

        


def main():
    root = tk.Tk()
    root.geometry("720x540")
    root.anchor("n")
    app = AppPanel(root)
    root.mainloop()

if __name__ == "__main__":
    main()