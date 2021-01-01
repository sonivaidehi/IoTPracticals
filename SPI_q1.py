import spidev
import time
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 115200
i = 0
try:
    while True:
        print("======= start ====")
        #print(i)
        #spi.writebytes([0x4, 0x061])
        time.sleep(1)
        resp = spi.readbytes(3)
        if(resp!= 255):
            value = resp[0] + resp[1] + resp[2]
            print(value)
            byte1 = bin(resp[0])[2:].rjust(8,'0')
            byte2 = bin(resp[1])[2:].rjust(8,'0')
            byte3 = bin(resp[2])[2:].rjust(8,'0')
            bits = byte1 + byte2 + byte3
            print(bits)
        i+=1
except KeyboardInterrupt:
    spi.close()
