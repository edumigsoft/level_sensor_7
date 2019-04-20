from machine import Pin

pin = Pin(2, Pin.OUT)

pin.value(1)

#via terminal OK
#python webrepl_cli.py blink.py -p python 192.168.0.4:/blink.py
#./webrepl_cli.py blink.py -p python 192.168.0.4:/blink.py