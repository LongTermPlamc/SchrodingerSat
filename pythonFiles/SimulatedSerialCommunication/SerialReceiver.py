# # receiver.py

# import serial
# import threading
# import time
# import keyboard

# def receive_messages():
#     # Emulate a GUI receiving messages via serial communication
#     with serial.Serial('COM8', baudrate=9600, timeout=1) as ser:
#         loop =True
#         while loop:
#             message = ser.readline().decode().strip()
#             print(f"Received: {message}")
#             time.sleep(2)
#             if 

# # Start a separate thread for receiving messages
# receiver_thread = threading.Thread(target=receive_messages)
# receiver_thread.start()

# # The GUI part of the code can be implemented here
# # For simplicity, we'll just wait for the receiver thread to finish
# receiver_thread.join()

# receiver.py

import serial
import threading
import tkinter as tk
import time

class ReceiverGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Serial Receiver")
        self.message_display = tk.Text(self.root, height=10, width=40)
        self.message_display.pack()
        
    def receive_messages(self):
        # Emulate a GUI receiving messages via serial communication
        with serial.Serial('COM8', baudrate=9600, timeout=1) as ser:
            while True:
                message = ser.readline().decode().strip()
                print(f"Received: {message}")
                self.message_display.insert(tk.END, f"{message}\n")
                self.message_display.see(tk.END)  # Auto-scroll to the bottom
            

    def start(self):
        # Start a separate thread for receiving messages
        receiver_thread = threading.Thread(target=self.receive_messages)
        receiver_thread.start()
        # Start the GUI main loop
        self.root.mainloop()

# Instantiate and start the GUI
receiver_gui = ReceiverGUI()
receiver_gui.start()