
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)



import os, time

edgetpu=1 # If Coral USB Accelerator connected, then make it '1' otherwise '0'

m1_1 = 8
m1_2 = 11
m2_1 = 14 
m2_2 = 15 
cam_light = 17
headlight_right = 18
headlight_left = 27 
sp_light=9 
pin20=20
pin21=21


      



def init_gpio():
 GPIO.setmode(GPIO.BCM)
 GPIO.setup(m1_1,GPIO.OUT)
 GPIO.setup(m1_2,GPIO.OUT)
 GPIO.setup(m2_1,GPIO.OUT)
 GPIO.setup(m2_2,GPIO.OUT)
 GPIO.setup(cam_light,GPIO.OUT)
 GPIO.setup(headlight_right,GPIO.OUT)
 GPIO.setup(headlight_left,GPIO.OUT)
 GPIO.setup(sp_light,GPIO.OUT)
 GPIO.setup(20, GPIO.OUT)# set GPIO 20 as output pin
 GPIO.setup(21, GPIO.OUT)# set GPIO 21 as output pin
      
 pin20 = GPIO.PWM(20, 100)    # create object pin20 for PWM on port 20 at 100 Hertz  
 pin21 = GPIO.PWM(21, 100)    # create object pin21 for PWM on port 21 at 100 Hertz  
 val=50 # maximum speed BJ changed to 50 from 100
 pin20.start(50)              # start pin20 on 0 percent duty cycle (off)  
 pin21.start(50)              # start pin21 on 0 percent duty cycle (off)  
    
 print("speed set to: ", val)


def back():
 pin20 = GPIO.PWM(20, 100)    # create object pin20 for PWM on port 20 at 100 Hertz  
 pin21 = GPIO.PWM(21, 100)    # create object pin21 for PWM on port 21 at 100 Hertz  
 pin20.start(50)              # start pin20 on 0 percent duty cycle (off)  
 pin21.start(50)    
 print("moving back!!!!!!")
 GPIO.output(m1_1, False)
 GPIO.output(m1_2, True)
 GPIO.output(m2_1, True)
 GPIO.output(m2_2, False)
 pin20.ChangeDutyCycle(35)
 pin21.ChangeDutyCycle(35)
 time.sleep(0.05)
 GPIO.cleanup()

    
def right():
 pin20 = GPIO.PWM(20, 100)    # create object pin20 for PWM on port 20 at 100 Hertz  
 pin21 = GPIO.PWM(21, 100)    # create object pin21 for PWM on port 21 at 100 Hertz  
 pin20.start(50)              # start pin20 on 0 percent duty cycle (off)  
 pin21.start(50)
 GPIO.output(m1_1, True)
 GPIO.output(m1_2, False)
 GPIO.output(m2_1, True)
 GPIO.output(m2_2, False)
 pin20.ChangeDutyCycle(35)
 pin21.ChangeDutyCycle(((val/2)+50))
 time.sleep(0.05)
 GPIO.cleanup()

def left():
 pin20 = GPIO.PWM(20, 100)    # create object pin20 for PWM on port 20 at 100 Hertz  
 pin21 = GPIO.PWM(21, 100)    # create object pin21 for PWM on port 21 at 100 Hertz  
 pin20.start(50)              # start pin20 on 0 percent duty cycle (off)  
 pin21.start(50)
 GPIO.output(m1_1, False)
 GPIO.output(m1_2, True)
 GPIO.output(m2_1, False)
 GPIO.output(m2_2, True)
 pin20.ChangeDutyCycle(((val/2)+50))
 pin21.ChangeDutyCycle(35)
 time.sleep(0.05)
 GPIO.cleanup()

def forward():
 pin20 = GPIO.PWM(20, 100)    # create object pin20 for PWM on port 20 at 100 Hertz  
 pin21 = GPIO.PWM(21, 100)    # create object pin21 for PWM on port 21 at 100 Hertz  
 pin20.start(50)              # start pin20 on 0 percent duty cycle (off)  
 pin21.start(50)
 GPIO.output(m1_1, True)
 GPIO.output(m1_2, False)
 GPIO.output(m2_1, False)
 GPIO.output(m2_2, True)
 pin20.ChangeDutyCycle(((val/2)+50))
 pin21.ChangeDutyCycle(((val/2)+50))
 time.sleep(0.05)
 GPIO.cleanup()

def stop():
 pin20 = GPIO.PWM(20, 100)    # create object pin20 for PWM on port 20 at 100 Hertz  
 pin21 = GPIO.PWM(21, 100)    # create object pin21 for PWM on port 21 at 100 Hertz  
 pin20.start(50)              # start pin20 on 0 percent duty cycle (off)  
 pin21.start(50)
 GPIO.output(m1_1, False)
 GPIO.output(m1_2, False)
 GPIO.output(m2_1, False)
 GPIO.output(m2_2, False)
 pin20.ChangeDutyCycle(55)
 pin21.ChangeDutyCycle(55)
 time.sleep(0.05)
 GPIO.cleanup()

def speak_tts(text,gender):
 cmd="python /var/www/html/earthrover/speaker/speaker_tts.py '" + text + "' " + gender + " &"
 os.system(cmd)

def camera_light(state):
 if(state=="ON"):
  GPIO.output(cam_light, True)
   #print("light on")
 else:
  GPIO.output(cam_light, False)
   #print("light off")

def head_lights(state):
 if(state=="ON"):
  GPIO.output(headlight_left, True)
  GPIO.output(headlight_right, True)
   #print("light on")
 else:
  GPIO.output(headlight_left, False)
  GPIO.output(headlight_right, False)
   #print("light off")

def red_light(state):
 if(state=="ON"):
  GPIO.output(sp_light, True)
   #print("light on")
 else:
  GPIO.output(sp_light, False)
   #print("light off")

