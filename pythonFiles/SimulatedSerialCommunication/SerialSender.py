# continuous_sender.py
import serial
import time
import random

def send_message(message_type):
    # Emulate a device sending messages via serial communication
    with serial.Serial('COM5', baudrate=9600, timeout=1) as ser:
        while True:
            data = str(random.uniform(20, 30))
            message = f"{message_type}:{data}"
            print(f"Sending: {message}")
            ser.write(message.encode())
            time.sleep(2)  # Simulating some delay between messages

# Example: Sending messages continuously
send_message("Temperature")