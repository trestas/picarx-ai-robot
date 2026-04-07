#!/usr/bin/env bash
set -euo pipefail

echo "==== Stage 03 hardware stack check ===="

echo "[1] Python:"
python3 --version

echo
echo "[2] pip user packages:"
python3 -m pip list | grep -E "robot-hat|picar-x|picarx|PyYAML" || true

echo
echo "[3] I2C buses:"
ls /dev/i2c* || true

echo
echo "[4] i2cdetect availability:"
which i2cdetect || true

echo
echo "[5] GPIO devices:"
ls /dev/gpiochip* || true

echo
echo "[6] Robot vendor dirs:"
ls -la ~/vendor || true

echo
echo "[7] Python import test:"
python3 - <<'PY'
mods = ["robot_hat"]
for m in mods:
    try:
        __import__(m)
        print(f"OK import: {m}")
    except Exception as e:
        print(f"FAIL import: {m} -> {e}")
PY

echo
echo "==== Stage 03 check complete ===="