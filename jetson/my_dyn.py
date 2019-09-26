import time
from pyax12.connection import Connection
import json

class Dynamixelka:
	def __init__(self, Serial):
#		config_file = open('control.json', 'r')
		try:
			config_file = open('control.json', 'r')
			conf = json.loads(config_file.read())
			self.freq = int(conf['steering']['freq'])
			self.left = conf['steering']['left']
			self.right = conf['steering']['right']
			self.middle = conf['steering']['mid']
			self.coef_l = (self.middle - self.left)/100
			self.coef_r = (self.right - self.middle)/100
		finally:
		    config_file.close()
		self.dyn = Connection(port=Serial, baudrate=57142)
		self.ID = 1
		self.voltage = 11
		self.pos_get_nomap = self.middle 
		self.load = 0
		try:
			self.voltage = self.dyn.get_present_voltage(self.ID)
		except:
			print("ErrorDyn")
		time.sleep(0.1)
		try:
			self.load = self.dyn.get_present_load(self.ID)
		except:
			print("ErrorDyn")
		time.sleep(0.1)
		try:
			self.pos_get_nomap = self.dyn.get_present_position(self.ID)
		except:
			print("ErrorDyn")
		time.sleep(0.1)
		self.position_get()
		self.position_set(0)
		self.life = False

	def reconfig():
		config_file = open('control.json', 'r')
		try:
			conf = json.loads(config_file.read())
			self.freq = int(conf['steering']['freq'])
			self.left = conf['steering']['left']
			self.right = conf['steering']['right']
			self.middle = conf['steering']['mid']
			self.coef_l = (self.middle - self.left)/100
			self.coef_r = (self.right - self.middle)/100
		finally:
		    config_file.close()

	def position_set(self, pos):		
		self.pos_set = pos
		if pos == 0:
			self.pos_set_nomap = self.middle
		elif pos < 0:
			self.pos_set_nomap = self.coef_l * pos + self.middle
		elif pos > 0:
			self.pos_set_nomap = self.coef_r * pos + self.middle
		else:
			print("position_set Wtf?")
		return self.pos_set_nomap

	def position_get(self, ):
		if self.pos_get_nomap == self.middle:
			self.pos_get = 0
		elif self.pos_get_nomap < self.middle:
			self.pos_get = (self.pos_get_nomap - self.middle) / self.coef_l
		elif self.pos_get_nomap > self.middle:
			self.pos_get = int((self.pos_get_nomap - self.middle) / self.coef_r)
		else:
			print("position_get Wtf?")
		return self.pos_get
	
	def loop(self):
		time_future = (int(time.time()*self.freq) + 1)%10
		self.life = True
		while self.life:
			time_now = (int(time.time()*self.freq))%10
			if (time_now == time_future):
				time_future = (time_now + 1) % 10
				#print(time.time())
				#try:
				#	self.pos_get_nomap = self.dyn.get_present_position(self.ID)
				#except:
				#	print("ErrorDyn")
				#print(self.pos_get_nomap )
				#print(self.position_get())
				time.sleep(0.05)
				try:
					#self.load = self.dyn.get_present_load(self.ID)
					self.dyn.goto(self.ID,int(self.pos_set_nomap),1023)
					#print(self.load)
				except:
					print("ErrorWrite: " + str(time.time()))
				""""
				time.sleep(0.075)
				try:
					self.voltage = self.dyn.get_present_voltage(self.ID)
				except:
					print("ErrorDyn")
				time.sleep(0.075)
				try:
					self.load = self.dyn.get_present_load(self.ID)
				except:
					print("ErrorDyn")"""
				#self.voltage = self.dyn.get_present_voltage(self.ID)
				#print(self.voltage)
				#time.sleep(0.01)
				#self.load = self.dyn.get_present_load(self.ID)
				#print(self.load)
				#print(self.dyn.goto(self.ID,int(self.pos_set_nomap),512))
		self.dyn.close()	


"""
if __name__ == "__main__":
	dyn = Dynamixelka("/dev/ttyUSB2")
	dyn.loop()
"""

		
		
