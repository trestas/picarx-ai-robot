#!/usr/bin/env python3
import time
from picarx import Picarx

SAFE_DISTANCE = 25

px = Picarx()

def follow_line(data):
    left, mid, right = data

    if mid < 400:
        px.set_dir_servo_angle(0)
        px.forward(20)
    elif left < mid:
        px.set_dir_servo_angle(-15)
        px.forward(18)
    elif right < mid:
        px.set_dir_servo_angle(15)
        px.forward(18)
    else:
        px.stop()

try:
    while True:
        distance = px.get_distance()

        if distance > 0 and distance < SAFE_DISTANCE:
            print("STOP obstacle")
            px.stop()
            continue

        data = px.get_grayscale_data()
        print(f"{data} | {distance}")
        follow_line(data)

        time.sleep(0.1)

except KeyboardInterrupt:
    px.stop()