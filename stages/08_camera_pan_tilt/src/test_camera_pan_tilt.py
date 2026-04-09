#!/usr/bin/env python3
import sys
import time
from pathlib import Path

HOME = Path("/home/arvydas")
VENV_SITE = HOME / "03_picarx_base_hw" / ".venv" / "lib" / "python3.12" / "site-packages"
VENDOR_PICARX = HOME / "vendor" / "picar-x"
VENDOR_ROBOT_HAT = HOME / "vendor" / "robot-hat"

for p in [str(VENV_SITE), str(VENDOR_PICARX), str(VENDOR_ROBOT_HAT)]:
    if p not in sys.path:
        sys.path.insert(0, p)

from picarx import Picarx

px = Picarx()

sequence = [
    ("pan_center", 0, None),
    ("pan_left", -25, None),
    ("pan_right", 25, None),
    ("pan_center", 0, None),
    ("tilt_down", None, -20),
    ("tilt_up", None, 20),
    ("tilt_center", None, 0),
]

try:
    for name, pan, tilt in sequence:
        print(f"Step: {name}")
        if pan is not None:
            px.set_cam_pan_angle(pan)
        if tilt is not None:
            px.set_cam_tilt_angle(tilt)
        time.sleep(1.0)
finally:
    px.set_cam_pan_angle(0)
    px.set_cam_tilt_angle(0)
    print("Pan/tilt test done.")
