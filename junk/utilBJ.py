
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
 GPIO.setup(cam_light,GPIO.OUT)
 GPIO.setup(headlight_right,GPIO.OUT)
 GPIO.setup(headlight_left,GPIO.OUT)
 GPIO.setup(sp_light,GPIO.OUT)

    
def back():
 print("moving back")
 
    
def right():
 print("moving right")

def left():
  print("moving left")

def forward():
 print("moving forward")

def stop():
 print("stop")


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

