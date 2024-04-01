from tkinter import ttk
import tkinter as tk

class AppPanel:

    def __init__(self, master):
        self.master = master
        self.master.title("SchrodingerSat")

        self.frame = tk.Frame(self.master, padx=20, pady=20)
        self.frame.pack(expand=True,fill="both")

        ##Serial conection panel
        zone1 = tk.Frame(self.frame, bg="lightblue",width=180,height=270)
        zone1.pack(expand=True, anchor="nw", fill="none")

        panelName = tk.Label(zone1, text="Serial Connection Panel")
        panelName.pack(anchor="nw",padx = 10, pady=5, ipady=5)
        comSelect = ttk.Combobox(zone1,values =[1,2,3,4],width=60)
        comSelect.pack(side="top",anchor="w", pady=2, padx=10, ipadx=5)
        baudSelect = tk.Entry(zone1,width=63)
        baudSelect.pack(side="top",anchor="w",pady=2, padx=10, ipadx=5)

        zone2 = tk.Frame(zone1,bg = "lightblue",width=100,height=100)
        zone2.pack(side="left", padx=10, pady=5)
        self.connectButton = tk.Button(zone2,text="Connect",fg="black",command=self.connect)
        self.connectButton.pack(side="left",padx=5,ipadx=10)
        self.disconnectButton = tk.Button(zone2,text="Disconnect",fg="black",command=self.disconnect, state=tk.DISABLED)
        self.disconnectButton.pack(side="left",padx =5,ipadx=10)
        
    def connect(self):
        self.connectButton.config(state=tk.DISABLED)
        self.disconnectButton.config(state=tk.NORMAL)
    
    def disconnect(self):
        self.connectButton.config(state=tk.NORMAL)
        self.disconnectButton.config(state=tk.DISABLED)
        


def main():
    root = tk.Tk()
    root.geometry("720x540")
    root.anchor("n")
    app = AppPanel(root)
    root.mainloop()

if __name__ == "__main__":
    main()