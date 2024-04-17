# continuous_sender.py
import serial
import time
import random

def send_message(message_type):
    # Emulate a device sending messages via serial communication
    with serial.Serial('COM5', baudrate=9600, timeout=1) as ser:
        while True:
            randData=random.randint(0, 100)
            data = f"({randData},10,10,10,10,10,10,10,10,10)\n"
            message = f"{data}"
            #print(f"Sending: {message}")
            dataagain=message.encode()
            ser.write(dataagain)
            time.sleep(0.02)  # Simulating some delay between messages

# Example: Sending messages continuously
send_message("Temperature")