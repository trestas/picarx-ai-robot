#!/usr/bin/env bash
set -euo pipefail

OUT_DIR="$HOME/picarx-ai-robot/stages/08_camera_pan_tilt/artifacts"
mkdir -p "$OUT_DIR"

if [ -e /dev/video0 ]; then
  echo "Using V4L2 /dev/video0"
  ffmpeg -y -f video4linux2 -i /dev/video0 -frames:v 1 "$OUT_DIR/camera_snapshot.jpg"
  echo "Saved: $OUT_DIR/camera_snapshot.jpg"
  exit 0
fi

if command -v libcamera-still >/dev/null 2>&1; then
  echo "Using libcamera-still"
  libcamera-still -n -o "$OUT_DIR/camera_snapshot.jpg"
  echo "Saved: $OUT_DIR/camera_snapshot.jpg"
  exit 0
fi

echo "ERROR: no working camera path found"
exit 1
