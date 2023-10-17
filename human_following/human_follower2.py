"""
The code in this file is same as 'human_follower.py' file. However, code with respect to FLASK implementation has been removed.
So there is no streaming of camera view. This is bare minimum human following robot.
"""
from pysabertooth import Sabertooth
motor= Sabertooth("/dev/serial0",baudrate=38400,address=128)
motor.drive(1,0)
motor.drive(2,0)  #gets rid of any lingering movements

import common as cm
import cv2
import numpy as np
from PIL import Image
import time
from threading import Thread
import RPi.GPIO as GPIO

import sys
sys.path.insert(0, '/var/www/html/earthrover')
import util as ut
ut.init_gpio()
time.sleep(0.1)
GPIO.setwarnings(False)

f0 = open("/var/www/html/earthrover/control_panel/pwm/pwm1.txt", "r+")
str0 = f0.read(5)
f0.close()
str0=str0.strip()

duty=float(str0)

cap = cv2.VideoCapture(0)
threshold=0.30
top_k=5 #number of objects to be shown as detected
edgetpu=1

model_dir = '/var/www/html/all_models'
model = 'mobilenet_ssd_v2_coco_quant_postprocess.tflite'
model_edgetpu = 'mobilenet_ssd_v2_coco_quant_postprocess_edgetpu.tflite'
lbl = 'coco_labels.txt'

tolerance=0.1
x_deviation=0
y_max=0

object_to_track='person'



def track_object(objs,labels):
    
    #global delay
    global x_deviation, y_max, tolerance
    
    
    if(len(objs)==0):
        print("no objects to track")
        motor.stop()
        ut.red_light("OFF")
        return

    flag=0
    for obj in objs:
        lbl=labels.get(obj.id, obj.id)
        if (lbl==object_to_track):
            x_min, y_min, x_max, y_max = list(obj.bbox)
            flag=1
            break
        
    #print(x_min, y_min, x_max, y_max)
    if(flag==0):
        print("No Targets")
        return
        
    x_diff=x_max-x_min
    y_diff=y_max-y_min
         
    obj_x_center=x_min+(x_diff/2)
    obj_x_center=round(obj_x_center,3)
    
    obj_y_center=y_min+(y_diff/2)
    obj_y_center=round(obj_y_center,3)
    
    x_deviation=round(0.5-obj_x_center,3)
    y_max=round(y_max,3)
        
    print("{",x_deviation,y_max,"}")
   
    thread = Thread(target = move_robot)
    thread.start()
    

def move_robot():
    global x_deviation, y_max, tolerance
    
    y=1-y_max #distance from bottom of the frame
    
    if(abs(x_deviation)<tolerance):
        if(y<0.1):
            ut.red_light("ON")
            motor.stop()
            print("Target located")
    
        else:
            ut.red_light("OFF")
            motor.drive(1,(duty))
            motor.drive(2,(duty))
            print("Pursuing")
    
    
    else:
        ut.red_light("OFF")
        if(x_deviation>=tolerance):
            delay1=get_delay(x_deviation)
                
            motor.drive(1,0)
            motor.drive(2,21)
            time.sleep(delay1)
            #motor.stop()
            print("Left")
    
                
        if(x_deviation<=-1*tolerance):
            delay1=get_delay(x_deviation)
                
            motor.drive(1,21)
            motor.drive(2,0)
            time.sleep(delay1)
	    #motor.stop()
            print("Right")
    

def get_delay(deviation):
    
    deviation=abs(deviation)
    
    if(deviation>=0.4):
        d=0.080
    elif(deviation>=0.35 and deviation<0.40):
        d=0.060
    elif(deviation>=0.20 and deviation<0.35):
        d=0.050
    else:
        d=0.040
    
    return d

def main():
  
    interpreter, labels =cm.load_model(model_dir,model_edgetpu,lbl,edgetpu)
    
    fps=1
   
    while True:
        start_time=time.time()
        
        #----------------Capture Camera Frame-----------------
        ret, frame = cap.read()
        if not ret:
            break
        
        cv2_im = frame
        cv2_im = cv2.flip(cv2_im, 0)
        cv2_im = cv2.flip(cv2_im, 0)

        cv2_im_rgb = cv2.cvtColor(cv2_im, cv2.COLOR_BGR2RGB)
        pil_im = Image.fromarray(cv2_im_rgb)
       
        #-------------------Inference---------------------------------
        cm.set_input(interpreter, pil_im)
        interpreter.invoke()
        objs = cm.get_output(interpreter, score_threshold=threshold, top_k=top_k)
        
        #-----------------other------------------------------------
        track_object(objs,labels)#tracking  <<<<<<<
       
        fps = round(1.0 / (time.time() - start_time),1)
        print("*********FPS: ",fps,"************")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

