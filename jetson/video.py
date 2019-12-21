import time
import os

class WebCam:
	def __init__(self):
		self.init = 1
		self.timestamp = int(time.time())

	def video0(self):
		os.system("ffmpeg -f v4l2 -framerate 25 -video_size 640x480 -input_format mjpeg -i /dev/video0 -y /home/mule/videos/video0_"+ str(self.timestamp) + ".mkv")
	def video4(self):
		os.system("ffmpeg -f v4l2 -framerate 25 -video_size 640x480 -input_format mjpeg -i /dev/video4 -y /home/mule/videos/video4_"+ str(self.timestamp) + ".mkv")
