#!/usr/bin/env bash
set -euo pipefail

echo "==== First boot prep ===="

sudo apt update
sudo apt -y upgrade

sudo apt -y install \
  openssh-server \
  curl wget git vim nano \
  net-tools ca-certificates \
  software-properties-common \
  bash-completion rsync htop tmux tree \
  python3 python3-pip

sudo systemctl enable ssh || true
sudo systemctl start ssh || true

echo "==== DONE ===="
