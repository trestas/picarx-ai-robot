#!/usr/bin/env python3
import time
from picarx import Picarx

SAFE_DISTANCE_CM = 25
DRIVE_SPEED = 18

px = Picarx()

try:
    while True:
        d = px.get_distance()
        print(f"Distance: {d} cm")

        if d > 0 and d <= SAFE_DISTANCE_CM:
            print("STOP: obstacle detected")
            px.stop()
        else:
            px.forward(DRIVE_SPEED)

        time.sleep(0.2)

except KeyboardInterrupt:
    px.stop()
    print("Stopped by user.")