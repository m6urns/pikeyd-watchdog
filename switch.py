import RPi.GPIO as GPIO
#import pexpect
import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('False')
        time.sleep(0.2)
    else: 
	if input_state == True:
           os.spawnl(os.P_NOWAIT, 'pikeyd restart')
           time.sleep(0.2)
            

