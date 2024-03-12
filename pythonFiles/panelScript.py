import tkinter as tk

class AppPanel:
    def __init__(self, master):
        self.master = master
        self.master.title("SchrodingerSat")

        #Frame to contain widgets
        self.frame = tk.Frame(self.master, padx = 20, pady = 20)
        self.frame.pack(expand=True, fill="both")

        #canva division
        zone1 = tk.Frame(self.frame, bg="lightblue",width=500,height=800)
        zone1.pack(side="left",expand=True,fill="x")

        zone2 = tk.Frame(self.frame, bg="lightgreen",width=200,height=20)
        zone2.pack(side="left", fill="both",expand=False)

        zone3 = tk.Frame(self.frame, bg="lightcoral",width=200,height=200)
        zone3.pack(side="right", fill="both",expand=False)

        # Create a canvas
        self.canvas = tk.Canvas(zone1, bg="white", width=100, height=100)
        self.canvas.pack(expand=False,fill="none")

        # Draw a rectangle on the canvas
        self.canvas.create_rectangle(50, 50, 80, 80, fill="lightblue",activefill="red")
        

def main():
    root = tk.Tk()
    root.geometry("1902x1080")
    root.anchor("center")
    app = AppPanel(root)
    root.mainloop()

if __name__ == "__main__":
    main()
