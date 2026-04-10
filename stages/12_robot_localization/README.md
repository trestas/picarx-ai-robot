# Stage 12 – Robot Localization (EKF IMU)

## Tikslas
Sukurti bazinę roboto lokalizaciją naudojant IMU duomenis ir Extended Kalman Filter (EKF).

## Naudojami komponentai
- robot_localization (ekf_node)
- BNO055 IMU
- ROS2 Jazzy
- Cyclone DDS (rmw_cyclonedds_cpp)

## Įėjimo duomenys
- /imu (sensor_msgs/msg/Imu)

## Išėjimo duomenys
- /odometry/filtered (nav_msgs/msg/Odometry)
- TF: odom → base_link

## Konfigūracija
Failas: ~/12_robot_localization/config/ekf_imu.yaml
Naudojamas tik:
- yaw (orientation z)
- angular velocity z
- ax, ay, az

## Paleidimas

# 1. Middleware
	export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
# 2. IMU node
	sudo -E bash -c "source /opt/ros/jazzy/setup.bash && export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp && source ~/ros2_ws/install/setup.bash && ros2 run picarx_control imu_node"
# 3. EKF
	ros2 run robot_localization ekf_node --ros-args --params-file ~/12_robot_localization/config/ekf_imu.yaml
# Testavimas
	ros2 topic echo --once /odometry/filtered
	ros2 topic hz /odometry/filtered
	ros2 run tf2_ros tf2_echo odom base_link
# Rezultatas
Stabilus ~10 Hz odometry stream
TF medis su odom → base_link
Orientacija sekama pagal IMU
# Pastabos
Pozicija (x,y) lieka 0 → reikės wheel odometry arba SLAM
Cyclone DDS būtinas dėl Fast DDS SHM problemų
