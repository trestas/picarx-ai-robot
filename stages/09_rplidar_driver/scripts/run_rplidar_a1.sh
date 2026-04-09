#!/usr/bin/env bash
set -eo pipefail

source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash

ros2 run sllidar_ros2 sllidar_node --ros-args \
  -p channel_type:=serial \
  -p serial_port:=/dev/ttyUSB0 \
  -p serial_baudrate:=115200 \
  -p frame_id:=laser \
  -p inverted:=false \
  -p angle_compensate:=true \
  -p scan_mode:=Sensitivity
