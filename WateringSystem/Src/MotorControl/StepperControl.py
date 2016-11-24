'''
Created on 24Nov.,2016

@author: kilta
'''
#!/usr/bin/env python
import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
p = GPIO.PWM(24, 500)
#Note: One revolution seems to be around 340 steps
def SpinMotor(direction, num_steps):
        GPIO.output(23, direction)
        while num_steps > 0:
                p.start(1)
                time.sleep(0.01)
                num_steps -= 1
        p.stop()
        GPIO.cleanup()
        return True


