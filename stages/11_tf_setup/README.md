# Etapas 11 – TF struktūra ir pasiruošimas sensor fusion

## 1. Etapo paskirtis
Sukurti roboto bazinį frame medį, kuris reikalingas tolimesnei lokalizacijai, sensor fusion ir SLAM.

## 2. Kas padaryta
Sukurti statiniai transform'ai tarp:
- `base_link` ir `laser`
- `base_link` ir `imu_link`
- `base_link` ir `camera_frame`

## 3. Naudojami frame
- `base_link`
- `laser`
- `imu_link`
- `camera_frame`

## 4. Paskirtis
Ši struktūra reikalinga tam, kad:
- lidar duomenys būtų susieti su roboto baze
- IMU duomenys būtų interpretuojami roboto koordinačių sistemoje
- kamera būtų įtraukta į bendrą roboto geometriją

## 5. Naudoti failai
- `config/static_transforms.yaml`
- `launch/static_tf_launch.py`
- `README.md`
- `config.json`
- `artifacts/stage11-notes.txt`

## 6. Etapo rezultatas
Sukurtas bazinis TF medis, paruošiantis robotą sensor fusion ir `robot_localization` etapui.

## 7. Kitas etapas
12 – robot_localization / EKF bazė
