#!/usr/bin/env python3
import os
import time

STEERING_CENTER = int(os.getenv("STEERING_CENTER", "0"))
STEERING_LEFT = int(os.getenv("STEERING_LEFT_LIMIT", "-15"))
STEERING_RIGHT = int(os.getenv("STEERING_RIGHT_LIMIT", "15"))

SPEED = int(os.getenv("DRIVE_TEST_SPEED", "18"))
FWD_SEC = float(os.getenv("DRIVE_TEST_FORWARD_SEC", "1.2"))
BWD_SEC = float(os.getenv("DRIVE_TEST_BACKWARD_SEC", "1.0"))
ENABLE_GROUND_TEST = os.getenv("ENABLE_GROUND_TEST", "false").lower() == "true"

def main() -> int:
    from picarx import Picarx

    px = Picarx()
    px.set_dir_servo_angle(STEERING_CENTER)
    time.sleep(0.5)

    if not ENABLE_GROUND_TEST:
        print("ENABLE_GROUND_TEST=false. Running platform-safe short sequence only.")
    else:
        print("Ground test explicitly enabled.")

    print("Forward center")
    px.set_dir_servo_angle(STEERING_CENTER)
    px.forward(SPEED)
    time.sleep(FWD_SEC)
    px.stop()
    time.sleep(1.0)

    print("Forward slight left")
    px.set_dir_servo_angle(STEERING_LEFT)
    px.forward(SPEED)
    time.sleep(min(FWD_SEC, 1.0))
    px.stop()
    time.sleep(1.0)

    print("Forward slight right")
    px.set_dir_servo_angle(STEERING_RIGHT)
    px.forward(SPEED)
    time.sleep(min(FWD_SEC, 1.0))
    px.stop()
    time.sleep(1.0)

    print("Backward center")
    px.set_dir_servo_angle(STEERING_CENTER)
    px.backward(SPEED)
    time.sleep(BWD_SEC)
    px.stop()
    time.sleep(0.5)

    px.set_dir_servo_angle(STEERING_CENTER)
    print("Drive sequence complete.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())