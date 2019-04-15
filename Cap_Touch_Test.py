import time
import board
import busio
import adafruit_mpr121

i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

while True:
    time.sleep(0.075)
    if mpr121[5].value:
        print("Pin 5 touched!")