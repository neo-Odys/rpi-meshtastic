import meshtastic
import meshtastic.serial_interface
from luma.oled.device import sh1106
from luma.core.interface.serial import i2c
from luma.core.render import canvas

iface = None
channel_index = 1
max_display_lines = 4

serial = i2c(port=1, address=0x3C)
device = sh1106(serial)

def send_message(msg):
    iface.sendText(msg, channelIndex=channel_index)
    with canvas(device) as draw:
        draw.text((0, 0), "Message Sent:", fill="white")
        display_message(draw, msg)

def display_message(draw, msg):
    lines = [msg[i:i + 16] for i in range(0, len(msg), 16)]
    for i, line in enumerate(lines[:max_display_lines]):
        draw.text((0, 10 + i * 10), line, fill="white")

def setup_iface():
    global iface
    iface = meshtastic.serial_interface.SerialInterface("/dev/ttyUSB0")

def close_iface():
    if iface:
        iface.close()

try:
    setup_iface()
    while True:
        msg = input("Enter message: ")
        with canvas(device) as draw:
            draw.text((0, 0), "Typing:", fill="white")
            display_message(draw, msg)
        
        if msg.lower() == "exit":
            break
        
        send_message(msg)

except KeyboardInterrupt:
    pass
except Exception as e:
    pass
finally:
    close_iface()

