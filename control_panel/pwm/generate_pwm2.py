from time import sleep  # import sleep function from time module
from pysabertooth import Sabertooth
sleep(.01)
motor= Sabertooth("/dev/serial0",baudrate=38400,address=128)
motor.drive(1,0)
motor.drive(2,0)

#while True:
#    sleep(1)
