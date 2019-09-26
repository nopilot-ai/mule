import minimalmodbus
import serial
import time
from itertools import repeat
import json

print("Start modbus")

class Jetsonmodbus:
	def __init__(self, Serial):
		config_file = open('control.json', 'r')
		try:
			config_file = open('control.json', 'r')
			conf = json.loads(config_file.read())
			self.freq = int(conf['freq'])
			self.steering_l = conf['steering']['left']
			self.steering_r = conf['steering']['right']
			self.steering_mid = conf['steering']['mid']
			self.accel_forward = conf['acceleration']['max']
			self.accel_back = conf['acceleration']['min']
			self.accel_mid = conf['acceleration']['mid']
		finally:
		    	config_file.close()
		
		self.errors = 0
		self.steering = 0;
		self.accel = 0;
		self.mb = minimalmodbus.Instrument(Serial,1,minimalmodbus.MODE_RTU)
		self.mb.serial.baudrate = 115200         # Baud
		self.mb.serial.bytesize = 8
		self.mb.serial.parity   = serial.PARITY_NONE
		self.mb.serial.stopbits = 1
		self.mb.serial.timeout  = 1          # second
		self.mb.address = 1
		self.mb.clear_buffers_before_each_transaction = True
		self.registers = list(repeat(0, 29))
		try:
			self.mb.write_register(4, 1, 0)
			self.mb.write_register(3, 1, 0)
			
		except:
			print("HZ")
		
	def reconfig(self):
		config_file = open('control.json', 'r')
		config_file = open('control.json', 'r')
		try:
			config_file = open('control.json', 'r')
			conf = json.loads(config_file.read())
			self.freq = int(conf['freq'])
			self.steering_l = conf['steering']['left']
			self.steering_r = conf['steering']['right']
			self.steering_mid = conf['steering']['mid']
			self.accel_forward = conf['acceleration']['max']
			self.accel_back = conf['acceleration']['min']
			self.accel_mid = conf['acceleration']['mid']
		finally:
		    	config_file.close()

	def set_steering(self, data):
		#print (self.steering)
		if (data > 100):
			data = 100
		elif (data < -100):
			data = -100
		# (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
		self.steering = (data - (-100)) * (self.steering_r - self.steering_l) / (100 - (-100)) + self.steering_l
		#print ("Steering:" + str(data) + " " + str(self.steering))

	def set_acceleration(self, data):
		print (self.accel)
		if (data > 100):
			data = 100
		elif (data < -100):
			data = -100
		# (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
		self.accel = (data - (-100)) * (self.accel_forward - self.accel_back) / (100 - (-100)) + self.accel_back
		print ("accel" + str(data) + " " + str(self.accel))

	def loop(self):
		self.life = True
		while self.life:
			self.registers = self.mb.read_registers(0, 30)
			try:
				self.mb.write_register(6, self.steering)				
			except:
				self.errors = self.errors + 1
			try:
				self.mb.write_register(5, self.accel)				
			except:
				self.errors = self.errors + 1
			#print(self.registers)
			time.sleep(1/self.freq)

	def set_acceleration(self, gas):
		self.accel = gas

"""
if __name__ == "__main__":
	jetboard = jetsonmodbus("/dev/ttyUSB1")
	jetboard.loop()
"""
