import joy
import modbus
import threading
import os
import time
import subprocess
import datetime
import time

joypad = joy.JoyXbox()
joy_wait_time = 20
while joypad.find():
	time.sleep(0.5)
	if joy_wait_time:
		print("wait_joypad:" + str(joy_wait_time))
		joy_wait_time = joy_wait_time - 1
	else:
		p = subprocess.Popen(["python3",  "/home/mule/mule/drive.py"])
		p.communicate() # remove this

jetboard = modbus.Jetsonmodbus("/dev/ttyUSB1")

thread_joystick = threading.Thread(target = joypad.read, name = "proc_joypad")
thread_modbus = threading.Thread(target = jetboard.loop, name = "proc_jetboard")
thread_joystick.start()
thread_modbus.start()

print("start car drive!!!")
while joypad.life:
	jetboard.set_control(joypad.steering, joypad.acceleration)
	#jetboard.set_acceleration()
	if joypad.btnLB:
		print("Reconfig")
		joypad.btnLB = 0
		jetboard.reconfig()
	if joypad.btnX:
		print("openCap")
		joypad.btnX = 0	
		jetboard.open_cap = 1
p.kill()
joypad.life = 0
jetboard.life = 0
print("end code")
