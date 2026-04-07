#!/usr/bin/env python3
import os
import time

CENTER = int(os.getenv("STEERING_CENTER", "0"))
LEFT = int(os.getenv("STEERING_LEFT_LIMIT", "-20"))
RIGHT = int(os.getenv("STEERING_RIGHT_LIMIT", "20"))

def main() -> int:
    from picarx import Picarx

    print("Creating Picarx instance...")
    px = Picarx()

    print(f"Centering steering to {CENTER}")
    px.set_dir_servo_angle(CENTER)
    time.sleep(1.0)

    print(f"Turning left to {LEFT}")
    px.set_dir_servo_angle(LEFT)
    time.sleep(1.0)

    print(f"Returning center to {CENTER}")
    px.set_dir_servo_angle(CENTER)
    time.sleep(1.0)

    print(f"Turning right to {RIGHT}")
    px.set_dir_servo_angle(RIGHT)
    time.sleep(1.0)

    print(f"Returning center to {CENTER}")
    px.set_dir_servo_angle(CENTER)
    time.sleep(1.0)

    print("Servo center test complete.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())