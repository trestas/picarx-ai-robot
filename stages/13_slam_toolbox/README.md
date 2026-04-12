# Stage 13 – SLAM Toolbox Mapping

## Tikslas
Paleisti realaus laiko 2D SLAM naudojant RPLidar A1M8, jau veikiančią TF grandinę ir EKF bazę.

## Naudojami komponentai
- slam_toolbox
- RPLidar A1M8
- robot_localization (EKF)
- ROS2 Jazzy
- Cyclone DDS (`rmw_cyclonedds_cpp`)

## Reikalingi įėjimai
- `/scan`
- TF:
  - `base_link -> laser`
  - `odom -> base_link`

## SLAM išėjimai
- `/map`
- `/map_metadata`
- TF:
  - `map -> odom`

## Patvirtintas veikimas
Patikrinta:
- `/scan` turi `Subscription count: 1`
- `/map` publikuojamas
- `map -> odom` veikia
- `odom -> base_link` veikia
- todėl bendra grandinė:
  - `map -> odom -> base_link -> laser`

## Paleidimo tvarka

### 1. Middleware
        source /opt/ros/jazzy/setup.bash
        export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

### 2. Static TF
        ros2 run tf2_ros static_transform_publisher 0 0 0.12 0 0 0 base_link laser
        ros2 run tf2_ros static_transform_publisher 0 0 0.05 0 0 0 base_link imu_link

### 3. IMU node
        sudo -E bash -c "source /opt/ros/jazzy/setup.bash && source /home/arvydas/ros2_ws/install/setup.bash && export >

### 4. EKF
        ros2 run robot_localization ekf_node --ros-args --params-file /home/arvydas/12_robot_localization/config/ekf_im>

### 5. LIDAR
Headless režimui naudoti launch failą be RViz:
        ros2 launch sllidar_ros2 sllidar_a1_launch.py

### 6. SLAM toolbox
        ros2 run slam_toolbox async_slam_toolbox_node --ros-args --params-file /home/arvydas/13_slam_toolbox/config/sla>

### 7. Lifecycle aktyvacija
        ros2 lifecycle set /slam_toolbox configure
        ros2 lifecycle set /slam_toolbox activate

### Testai
        ros2 topic info /scan
        ros2 topic list | grep map
        ros2 topic echo --once /map
        ros2 run tf2_ros tf2_echo map odom
        ros2 run tf2_ros tf2_echo odom base_link

### Rezultatas

SLAM bazė veikia:
žemėlapis generuojamas
TF grandinė pilna
robotas pasiruošęs žemėlapio išsaugojimui ir lokalizacijos režimui

### Pastabos
view_sllidar_a1_launch.py nerekomenduojamas headless režime, nes tempia RViz
naudoti sllidar_a1_launch.py arba kitą launch be RViz
slam_toolbox reikia lifecycle aktyvavimo (configure, activate)
naudojamas Cyclone DDS dėl Fast DDS SHM konfliktų
