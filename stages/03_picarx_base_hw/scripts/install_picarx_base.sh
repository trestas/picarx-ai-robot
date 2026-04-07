#!/usr/bin/env bash
set -euo pipefail

echo "==== Stage 03: install base hardware dependencies ===="

sudo apt update
sudo apt install -y \
  git \
  python3-pip \
  python3-venv \
  python3-dev \
  i2c-tools \
  python3-smbus \
  python3-gpiozero \
  python3-lgpio \
  libgpiod-dev \
  python3-yaml \
  python3-setuptools \
  python3-wheel \
  build-essential \
  portaudio19-dev \
  python3-dev

mkdir -p ~/vendor
cd ~/vendor

if [ ! -d robot-hat ]; then
  git clone https://github.com/sunfounder/robot-hat.git
fi

if [ ! -d picar-x ]; then
  git clone https://github.com/sunfounder/picar-x.git
fi

cd ~/vendor/robot-hat
python3 -m pip install --user -e .

cd ~/vendor/picar-x
python3 -m pip install --user -e . || true

echo "==== Installed base dependencies ===="
echo "Note: picar-x editable install may require adaptation on Ubuntu; custom stage scripts are the primary control path."