from pysabertooth import Sabertooth
motor= Sabertooth("/dev/serial0",baudrate=38400,address=128)
motor.drive(1,-20)
motor.drive(2,-20)
sleep(1)