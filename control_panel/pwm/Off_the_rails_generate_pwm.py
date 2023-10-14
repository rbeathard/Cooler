
import RPi.GPIO as GPIO 
from time import sleep  # import sleep function from time module

GPIO.setwarnings(False)
  
GPIO.setmode(GPIO.BCM)  # choose BCM numbering scheme  this method uses GPIO numbering vs countable pin numbering so numerically the 2nd pin on the left is GPIO2 and pin number 3
  
GPIO.setup(18, GPIO.OUT)# set GPIO 18 as output pin
GPIO.setup(19, GPIO.OUT)# set GPIO 19 as output pin
GPIO.setup(8, GPIO.OUT)# set GPIO 20 as output pin
GPIO.setup(11, GPIO.OUT)# set GPIO 21 as output pin
GPIO.setup(14, GPIO.OUT)# set GPIO 20 as output pin
GPIO.setup(15, GPIO.OUT)# set GPIO 21 as output pin
  
pin18 = GPIO.PWM(18, 100)    # create object pin20 for PWM on port 20 at 100 Hertz  
pin19 = GPIO.PWM(19, 100)    # create object pin21 for PWM on port 21 at 100 Hertz  

pin18.start(50)              # start pin20 on 0 percent duty cycle (off) 
pin19.start(50)              # start pin21 on 0 percent duty cycle (off) 


###### read the disk file pwm1.txt for speed value#########################
f0 = open("/var/www/html/earthrover/control_panel/pwm/pwm1.txt", "r+")
str0 = f0.read(5)
f0.close()
str0=str0.strip()

duty = float(str0)

  
##forward
if GPIO.input(8) is 1 and GPIO.input(11) is 0 and GPIO.input(14) is 0 and GPIO.input(15) is 1:
    
    pin18.ChangeDutyCycle(((duty / 2) + 50))
    pin19.ChangeDutyCycle(((duty / 2) + 50))
    print("duty= ",duty)

while True:
    sleep(1)

##backwards
if GPIO.input(8) is 0 and GPIO.input(11) is 1 and GPIO.input(14) is 1 and GPIO.input(15) is 0:
    
    pin18.ChangeDutyCycle(35)
    pin19.ChangeDutyCycle(35)
    print("duty= ",duty)

while True:
    sleep(1)

##Left
if GPIO.input(8) is 0 and GPIO.input(11) is 1 and GPIO.input(14) is 0 and GPIO.input(15) is 1:
    
    pin18.ChangeDutyCycle(((duty / 2) + 50))
    pin19.ChangeDutyCycle(35)
    print("duty= ",duty)

while True:
    sleep(1)

##Right
if GPIO.input(8) is 1 and GPIO.input(11) is 0 and GPIO.input(14) is 1 and GPIO.input(15) is 0:
    
    pin18.ChangeDutyCycle(35)
    pin19.ChangeDutyCycle(((duty / 2) + 50))
    print("duty= ",duty)

while True:
    sleep(1)

##Stop
if GPIO.input(8) is 0 and GPIO.input(11) is 0 and GPIO.input(14) is 0 and GPIO.input(15) is 0:
    
    pin18.ChangeDutyCycle(50)
    pin19.ChangeDutyCycle(50)
    print("duty= ",duty)

while True:
    sleep(1)
