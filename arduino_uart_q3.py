import serial
from time import sleep

if __name__ == '__main__':
    
    ser = serial.Serial('/dev/ttyACM0', 9600)
    
    ser.flush()
    while True:
        ser.write(0x1)
        if ser.in_waiting > 0: 
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
#             if(line == "0"):
#                 print("Arduino connected... but no data")
#             else:
#                 print("Not connected")
            
                