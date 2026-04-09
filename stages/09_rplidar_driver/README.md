# Etapas 09 – RPLidar A1M8 integracija

## 1. Etapo paskirtis
Integruoti RPLidar A1M8 į ROS 2 sistemą ir gauti `LaserScan` duomenis per `/scan`.

## 2. Kas padaryta
- prijungtas RPLidar A1M8 per USB adapterį
- sistema aptiko lidarą kaip `/dev/ttyUSB0` arba kitą `/dev/ttyUSB*`
- į `~/ros2_ws` įdiegtas `sllidar_ros2`
- pritaikyta A1 konfigūracija:
  - `serial_baudrate=115200`
  - `frame_id=laser`
  - `scan_mode=Sensitivity`
- paleistas `sllidar_node`
- patikrinta `/scan` tema

## 3. Svarbi pastaba
Naudojamas oficialus SLAMTEC ROS 2 paketas `sllidar_ros2`.
RViz šiame etape nėra būtinas; svarbiausia gauti stabilų `/scan`.

## 4. Naudoti failai
- `scripts/probe_rplidar_usb.sh`
- `scripts/run_rplidar_a1.sh`
- `configs/rplidar_a1_config.yaml`
- `artifacts/stage9-notes.txt`
- `README.md`
- `manifest.json`

## 5. Etapo rezultatas
RPLidar A1M8 sėkmingai integruotas į ROS 2, publikuojama `/scan` tema.

## 6. Kitas etapas
10 – BNO055 IMU integracija
