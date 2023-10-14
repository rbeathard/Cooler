
from pysabertooth import Sabertooth
motor= Sabertooth("/dev/serial0",baudrate=38400,address=128)
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

import os, time

edgetpu=1 # If Coral USB Accelerator connected, then make it '1' otherwise '0'
GPIO.setmode(GPIO.BCM) #BCM so use GPIO coded number      do not count pins


cam_light = 17 #Originally camera light but switching to emergency lighting?  could be Linear actuator control as well
headlight_right = 20
headlight_left = 27 #my thought is to only use 1 relay so this one not needed unless want to add additional lighting?  maybe softer red light?  colored LEDS?
sp_light=9 #Even though PWM interferes with speaker, leave this in as it also signals a stop command
 



def init_gpio():

    GPIO.setup(cam_light,GPIO.OUT)
    GPIO.setup(headlight_right,GPIO.OUT)
    GPIO.setup(headlight_left,GPIO.OUT)
    GPIO.setup(sp_light,GPIO.OUT)

###### read the disk file pwm1.txt for speed value#########################
f0 = open("/var/www/html/earthrover/control_panel/pwm/pwm1.txt", "r+")
str0 = f0.read(5)
f0.close()
str0=str0.strip()

duty = float(str0)


def back():
    motor.drive(1,-20)
    motor.drive(2,-20)
    print("Back")

def right():
    motor.drive(1,30)
    motor.drive(2,0)
    print("Right")

def left():
    motor.drive(1,0)
    motor.drive(2,30)
    print("Left")

def forward():
    motor.drive(1,(duty))
    motor.drive(2,(duty))
    print("Forward")

def stop():
    #motor.drive(1,0)
    #motor.drive(2,0)
    motor.stop()
    print("Stop")

def speak_tts(text,gender):
    cmd="python /var/www/html/earthrover/speaker/speaker_tts.py '" + text + "' " + gender + " &"
    os.system(cmd)

def camera_light(state):
    if(state=="ON"):
        GPIO.output(cam_light, True)
        print("Emergency")
    else:
        GPIO.output(cam_light, False)
        #print("Emergency")

def head_lights(state):
    if(state=="ON"):
        GPIO.output(headlight_left, True)
        GPIO.output(headlight_right, True)
        print("Headlightlight on")
    else:
        GPIO.output(headlight_left, False)
        GPIO.output(headlight_right, False)
        print("Headlight off")

def red_light(state):
    if(state=="ON"):
        GPIO.output(sp_light, True)
        print("Red light on")
    else:
        GPIO.output(sp_light, False)
        print("Red light off")
