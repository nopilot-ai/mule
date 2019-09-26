#import evdev
from evdev import InputDevice, categorize, ecodes
import time


class JoyXbox:
	def __init__(self):
		self.gamepad = 0
		self.drag = int(0)
		self.gas = int(0)
		self.acceleration = int(0)
		self.steering = int(0)
		self.life = int(0)
		self.update = False
		self.btnLB = 0
		self.btnRB = 0
		self.btnX = 0
		self.btnY = 0
		self.btnB = 0
		self.btnA = 0

	def find(self):
		try:
			for x in range(0,10):
				self.gamepad = InputDevice('/dev/input/event' + str(x))
				if self.gamepad.name.find("Xbox") != -1:
					return "/dev/input/event" + str(x)
			gamepad = 0
			return -1
		except:
			return -1
	
	def get_update(self):
		if self.update:
			self.update = False
			return True
		return False
	def read(self):
		try:
			self.life = int(1)
			for event in self.gamepad.read_loop():
				if self.life < 1:
					break
				if event.type == ecodes.EV_KEY:
					if event.code == 305:
						self.life = 0
						print("Stop joypad loop")
					
					if event.code == 307:
						if event.value == 0:
							self.btnLB = 1
					print(time.time())
					print(event.value)
					print(event.code)
				if event.type == 3:
					if (event.code == 0):
						self.steering = int(199/65536 * event.value - 99)
						self.update = True
						#print("X: ", int(self.steering))
					if (event.code == 2):
						self.drag = -event.value
						self.acceleration = int(100/1024 * (self.drag + self.gas))
						self.update = True
						#print("LT: ", self.acceleration)
					if (event.code == 5):
						self.gas = event.value
						self.acceleration = int(100/1024 * (self.drag + self.gas))
						self.update = True
						#print("RT: ", self.acceleration)
		except:
			print("joypad disconnect")
			self.life = -1
	
	
"""
if __name__ == "__main__":
	joy = JoyXbox()
	print(joy.find())
	joy.read()
"""


