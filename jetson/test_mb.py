import joy
import video
import modbus
import threading
import os
import time
import subprocess
import datetime

print("Start mb test")
jetboard = modbus.Jetsonmodbus("/dev/ttyUSB1")
thread_modbus = threading.Thread(target = jetboard.loop, name = "proc_jetboard")
thread_modbus.start()

while True:
	jetboard.set_control(0, 0)
jetboard.life = 0
print("end code")
