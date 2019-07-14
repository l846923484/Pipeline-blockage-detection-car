import RPi.GPIO as GPIO
from AlphaBot import AlphaBot
import os, time

Ab = AlphaBot()
DR = 16
DL = 19

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(DR,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(DL,GPIO.IN,GPIO.PUD_UP)

try:
	hasObstacle = False
	isBegin = False
	isEnd = False
	isPrint = False
	while True:
		DR_status = GPIO.input(DR)
		DL_status = GPIO.input(DL)
		if(not hasObstacle and (DL_status == 1) and (DR_status == 1)):
			Ab.forward()
			
			if not isBegin:
				isBegin = True
				begin = time.time()
				
			print("forward")
		elif(not hasObstacle and (DL_status == 1) and (DR_status == 0)):
			Ab.left()
			print("left")
		elif(not hasObstacle and (DL_status == 0) and (DR_status == 1)):
			Ab.right()
			print("right")
		else:
			if not isEnd:
				end = time.time()
				print("froward time: " + str(end-begin))
				print("distance:"+str((end-begin)*0.37175))
				isEnd = True
				
			hasObstacle = True
			Ab.backward()
			
			if not isPrint:
				print("backword")
				isPrint = True
		
		if '192' not in os.popen('ifconfig | grep 192').read():
			print '\n******out of distance******\n'
			hasObstacle = True
	
except KeyboardInterrupt:
	GPIO.cleanup();

