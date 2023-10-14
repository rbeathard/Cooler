import time
import serial
import sys

# interpolates the variable from input to output range
def lerp(x, min_in, max_in, min_out, max_out):
    return int(min_out + (x - min_in) * (max_out-min_out)/(max_in-min_in))

def motorA(speed):
    output = lerp(speed, -100, 100, 0, 127)
    Sabertooth_Serial.write(output.to_bytes(1, 'little'))

def motorB(speed):
    output = lerp(speed, -100, 100, 128, 255)
    Sabertooth_Serial.write(output.to_bytes(1, 'little'))


try:
    port_name = "/dev/serial0"
    baud_rate = 38400

    # Open Serial Port
    Sabertooth_Serial = serial.Serial(
        port=port_name, # SERIAL PORT on SBC 
        baudrate = baud_rate,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )

    motorA(20)
    motorB(20)    

    # Close Serial Port            
    #Sabertooth_Serial.close() 

except serial.SerialException as e:
    print(f"Error writing to serial port: {e}")