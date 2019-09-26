import joy
import modbus
import threading



joypad = joy.JoyXbox()
joypad_status = joypad.find()
print (joypad_status)
if joypad_status == -1:
	print("Joypad not find")
	raise SystemExit

jetboard = modbus.Jetsonmodbus("/dev/ttyUSB1")

thread_joystick = threading.Thread(target = joypad.read, name = "proc_joypad")
thread_modbus = threading.Thread(target = jetboard.loop, name = "proc_jetboard")
thread_joystick.start()
thread_modbus.start()
while joypad.life:
	jetboard.set_control(joypad.steering, joypad.acceleration)
	#jetboard.set_acceleration()
	if joypad.btnLB:
		print("Reconfig")
		joypad.btnLB = 0
		jetboard.reconfig()
joypad.life = 0
jetboard.life = 0
print("end code")
