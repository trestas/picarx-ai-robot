#!/usr/bin/env python3
import time
from picarx import Picarx

px = Picarx()

try:
    while True:
        d = px.get_distance()
        print(f"Distance: {d} cm")
        time.sleep(0.5)
except KeyboardInterrupt:
    px.stop()
    print("Stopped.")