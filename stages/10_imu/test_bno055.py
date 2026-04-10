import time
import board
import busio
import adafruit_bno055

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055_I2C(i2c)

while True:
    print("Euler:", sensor.euler)
    print("Quaternion:", sensor.quaternion)
    print("Accel:", sensor.linear_acceleration)
    print("-" * 40)
    time.sleep(1)
