import meshtastic
import meshtastic.serial_interface
import time
import datetime

iface = None
channel_index = 1

def send_message(msg):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg_with_time = f"{msg} - sent at {current_time}"
    iface.sendText(msg_with_time, channelIndex=channel_index)

def setup_iface():
    global iface
    iface = meshtastic.serial_interface.SerialInterface("/dev/ttyUSB0")

def close_iface():
    if iface:
        iface.close()

try:
    setup_iface()
    print("Program started. Enter a message and press Enter to send.")
    
    while True:
        msg = input("Enter message: ")
        if msg.lower() == "exit":
            print("Program terminated.")
            break
        send_message(msg)

except KeyboardInterrupt:
    print("Program interrupted (Ctrl+C).")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    close_iface()
    print("Program finished.")

