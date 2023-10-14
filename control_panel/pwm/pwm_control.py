
import os, time
from time import sleep  # import sleep function from time module

#from pysabertooth import Sabertooth
sleep(1)

#motor= Sabertooth("/dev/serial0",baudrate=38400,address=128)

os.system("python /var/www/html/earthrover/control_panel/pwm/generate_pwm.py")
print("started !!!")

sleep(1)

#print("starting pwm")
#os.system("python /var/www/html/earthrover/control_panel/pwm/generate_pwm.py &")
#print("started !!!")
