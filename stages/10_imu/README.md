# Etapas 10 – BNO055 IMU integracija

## 1. Etapo paskirtis
Integruoti BNO055 IMU jutiklį į ROS2 sistemą ir publikuoti roboto orientacijos bei judesio duomenis per `/imu`.

## 2. Kas padaryta
- patikrintas BNO055 veikimas per I2C
- sukurtas lokalus Python testas
- sukurtas ROS2 mazgas `imu_node`
- publikuojamas `/imu` topic

## 3. ROS rezultatas
Publikuojamas topic:

- `/imu` → `sensor_msgs/msg/Imu`

Publikuojami duomenys:
- orientation (quaternion)
- angular_velocity
- linear_acceleration

## 4. Dažnis
IMU duomenų publikavimo dažnis:
- apie 10 Hz

## 5. Techninė pastaba
Node paleidžiamas per `sudo`, nes aparatūros prieiga šioje sistemoje taip veikia patikimiausiai.

Paleidimo komanda:
```bash
sudo -E bash -c "source /opt/ros/jazzy/setup.bash && source /home/arvydas/ros2_ws/install/setup.bash && ros2 run picarx_control imu_node"

## 6. Naudoti failai
	~/10_imu/test_bno055.py
	~/ros2_ws/src/picarx_control/picarx_control/imu_node.py
	~/ros2_ws/src/picarx_control/setup.py
	README.md
	config.json
	stage10-notes.txt

## 7. Etapo rezultatas

BNO055 sėkmingai integruotas į ROS2 sistemą. Robotas dabar turi orientacijos ir judesio duomenų šaltinį, reikalingą sensor fusion ir tolimesniems SLAM / navigacijos etapams.

## 8. Kitas etapas

	11 – Sensor fusion / robot_localization pasiruošimas
