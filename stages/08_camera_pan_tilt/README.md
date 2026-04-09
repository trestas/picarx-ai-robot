# Etapas 08 – Kamera + Pan/Tilt + ROS image stream

## 1. Etapo paskirtis
Pilnai integruoti PiCar-X kamerą į roboto bazinę įrangą:
- pan/tilt servo valdymas
- userspace kamera per Raspberry Pi libcamera stack
- ROS image stream
- pasiruošimas web sąsajai

## 2. Kas padaryta
- subuildintas Raspberry Pi `libcamera` fork
- subuildinti `rpicam-apps`
- patvirtinta kamera `ov5647`
- veikia `rpicam-hello --list-cameras`
- veikia snapshot per `rpicam-still`
- veikia ROS pan/tilt node `camera_pt_node`
- subuildintas ir paleistas `camera_ros`
- publikuojami:
  - `/camera/image_raw`
  - `/camera/camera_info`
- paruoštas web stream per `web_video_server`

## 3. Svarbi techninė pastaba
Tiesioginis V4L2 kelias per `/dev/video0` ir `v4l2_camera` nebuvo pasirinktas kaip galutinis sprendimas.
Galutinis sprendimas:
- Raspberry Pi `libcamera` fork
- `rpicam-apps`
- `camera_ros`

## 4. Kamera
Aptikta kamera:
- `ov5647`

Userspace testai:
- `rpicam-hello --list-cameras`
- `rpicam-still`

## 5. Pan/Tilt
Valdymas atliekamas per `Picarx`:
- `set_cam_pan_angle()`
- `set_cam_tilt_angle()`

ROS topics:
- `/cmd_camera_pan`
- `/cmd_camera_tilt`

## 6. ROS kameros stream
Naudojamas `camera_ros` mazgas.

Publikuojami topic:
- `/camera/image_raw`
- `/camera/camera_info`

## 7. Web paruošimas
Naudojamas `web_video_server`.

Pavyzdinis stream URL:
  http://<ROBOT_IP>:8080/stream?topic=/camera/image_raw

## 8. Sukurti / naudoti failai
stages/08_camera_pan_tilt/scripts/camera_probe.sh
stages/08_camera_pan_tilt/scripts/camera_snapshot.sh
stages/08_camera_pan_tilt/src/test_camera_pan_tilt.py
stages/08_camera_pan_tilt/config.json
stages/08_camera_pan_tilt/artifacts/camera_snapshot.jpg
ros2_ws/src/picarx_control/picarx_control/camera_pt_node.py
camera_ws/src/camera_ros/...

## 9. Etapo rezultatas

Kamera pilnai integruota baziniam naudojimui:
	veikia pan/tilt
	veikia userspace kamera
	veikia ROS image stream
	paruoštas kelias web sąsajai
