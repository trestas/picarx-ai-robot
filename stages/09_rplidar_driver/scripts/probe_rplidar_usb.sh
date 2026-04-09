#!/usr/bin/env bash
set -eo pipefail

echo "=== ttyUSB devices ==="
ls -l /dev/ttyUSB* 2>/dev/null || true

echo
echo "=== last kernel messages ==="
dmesg | tail -n 80
