#!/usr/bin/env bash
set -euo pipefail

echo "==== Stage 01 OS check ===="

echo "[1] uname:"
uname -a

echo "[2] os-release:"
cat /etc/os-release

echo "[3] hostname:"
hostnamectl

echo "[4] network:"
hostname -I || true
ip addr || true

echo "[5] routes:"
ip route || true

echo "[6] SSH:"
systemctl status ssh --no-pager || true

echo "[7] disk:"
df -h

echo "[8] memory:"
free -h

echo "[9] uptime:"
uptime

echo "==== DONE ===="
