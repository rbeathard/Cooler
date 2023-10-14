import RPi.GPIO as GPIO
GPIO.setwarnings(False)

import os, time

edgetpu=1 # If Coral USB Accelerator connected, then make it '1' otherwise '0'
GPIO.setmode(GPIO.BCM) #BCM so use GPIO coded number      do not count pins


cam_light = 17 #Originally camera light but switching to emergency lighting?  could be Linear actuator control as well
headlight_right = 20
headlight_left = 27 #my thought is to only use 1 relay so this one not needed unless want to add additional lighting?  maybe softer red light?  colored LEDS?
sp_light=9 #Even though PWM interferes with speaker, leave this in as it also signals a stop command
GPIO.setup(12, GPIO.OUT)# set GPIO 12 as output pin previously 20  12 and 13 are PWM0 and PWM1
GPIO.setup(13, GPIO.OUT)# set GPIO 13 as output pin previouly 21
pin12=GPIO.PWM(12, 50)    # create object pin20 for PWM on port 20 at 100 Hertz  
pin13=GPIO.PWM(13, 50)    # create object pin21 for PWM on port 21 at 100 Hertz  



def init_gpio():
      
    val=duty # maximum speed  bj changed to 50 from 100   

    pin12.start(50)              # start pin20 on 50 percent duty cycle (off)  
    pin13.start(50)              # start pin21 on 50 percent duty cycle (off)  
    
    print("speed set to: ", val)

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
    pin12.ChangeDutyCycle(40)
    pin13.ChangeDutyCycle(40)
    print("Back")

def right():
    pin12.ChangeDutyCycle(50)              # start pin20 on 0 percent duty cycle (off)  
    pin13.ChangeDutyCycle(((duty/2)+50))              # start pin21 on 0 percent duty cycle (off) 
    print("Right")

def left():
    pin12.ChangeDutyCycle(((duty/2)+50))              # start pin20 on 0 percent duty cycle (off)  
    pin13.ChangeDutyCycle(50)              # start pin21 on 0 percent duty cycle (off)
    print("Left")

def forward():
    pin12.ChangeDutyCycle(((duty/2)+50))              # start pin20 on 0 percent duty cycle (off)  
    pin13.ChangeDutyCycle(((duty/2)+50))            # start pin21 on 0 percent duty cycle (off)
    print("Forward")

def stop():
    pin12.ChangeDutyCycle(50)              # start pin20 on 0 percent duty cycle (off)  
    pin13.ChangeDutyCycle(50)              # start pin21 on 0 percent duty cycle (off)
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
