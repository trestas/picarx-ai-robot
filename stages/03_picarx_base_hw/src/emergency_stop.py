#!/usr/bin/env python3
import sys
import time

def main() -> int:
    try:
        from picarx import Picarx
    except Exception as e:
        print(f"ERROR: cannot import Picarx: {e}")
        return 1

    px = Picarx()
    try:
        px.forward(0)
        px.backward(0)
    except Exception:
        pass

    try:
        px.stop()
    except Exception as e:
        print(f"WARNING: stop() failed: {e}")

    try:
        px.set_dir_servo_angle(0)
    except Exception as e:
        print(f"WARNING: set_dir_servo_angle(0) failed: {e}")

    time.sleep(0.2)
    print("Emergency stop sent.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())