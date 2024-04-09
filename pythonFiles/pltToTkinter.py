import tkinter as tk
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class AppPanel:
    def __init__(self, master):
        self.master = master
        self.master.title("App Panel")

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.text_label = tk.Label(self.frame, text="Time: ")
        self.text_label.grid(row=0, column=0)

        self.plot_frame = tk.Frame(self.frame)
        self.plot_frame.grid(row=1, column=0)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.plot_frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.update_time()
        self.update_plot()

    def update_time(self):
        current_time = time.strftime('%H:%M:%S')
        self.text_label.config(text="Time: " + current_time)
        self.master.after(1000, self.update_time)

    def update_plot(self):
        x = np.linspace(0, 10, 100)
        frequency = time.time() % 10  # Change frequency every second
        y = np.sin(frequency * x)

        self.ax.clear()
        self.ax.plot(x, y)
        self.ax.set_xlabel('X-axis')
        self.ax.set_ylabel('Y-axis')
        self.ax.set_title('Sine Wave')

        self.canvas.draw()

        self.master.after(1000, self.update_plot)  # Update plot every second

def main():
    root = tk.Tk()
    app = AppPanel(root)
    root.mainloop()

if __name__ == "__main__":
    main()
