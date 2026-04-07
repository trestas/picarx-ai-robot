#!/usr/bin/env python3
import os
import time

SPEED = int(os.getenv("MOTOR_TEST_SPEED", "20"))
DURATION = float(os.getenv("MOTOR_TEST_DURATION_SEC", "1.5"))

def safe_sleep():
    time.sleep(DURATION)

def main() -> int:
    from picarx import Picarx

    px = Picarx()

    print(f"Forward at speed {SPEED} for {DURATION}s")
    px.forward(SPEED)
    safe_sleep()
    px.stop()
    time.sleep(1.0)

    print(f"Backward at speed {SPEED} for {DURATION}s")
    px.backward(SPEED)
    safe_sleep()
    px.stop()
    time.sleep(1.0)

    print("Motor test complete.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())