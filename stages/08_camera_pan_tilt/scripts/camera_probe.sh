#!/usr/bin/env bash
set -euo pipefail

echo "=== /dev/video* ==="
ls -l /dev/video* 2>/dev/null || true

echo
echo "=== V4L2 devices ==="
v4l2-ctl --list-devices 2>/dev/null || true

echo
echo "=== libcamera cameras ==="
libcamera-hello --list-cameras 2>/dev/null || libcamera-still --list-cameras 2>/dev/null || true

echo
echo "=== media devices ==="
ls -l /dev/media* 2>/dev/null || true