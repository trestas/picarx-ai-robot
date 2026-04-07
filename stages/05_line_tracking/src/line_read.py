#!/usr/bin/env python3
import time
from picarx import Picarx

px = Picarx()

try:
    while True:
        data = px.get_grayscale_data()
        print(f"Line sensor: {data}")
        time.sleep(0.2)
except KeyboardInterrupt:
    print("Stopped.")