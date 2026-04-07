# Etapas 06 – Pirmas ROS2 Node integravimas

## 1. Etapo paskirtis
Perkelti roboto valdymo logiką į ROS2 node ir patikrinti, kad ROS aplinka gali:
- paleisti node
- pasiekti PiCar-X valdymo sluoksnį
- skaityti jutiklius
- vykdyti bazinę valdymo logiką

## 2. Ką turėjome etapo pradžioje
- ROS2 Jazzy bazę
- veikiantį PiCar-X valdymą per `Picarx`
- ultragarso jutiklį
- grayscale jutiklių prieigą

## 3. Kas padaryta
- sukurtas ROS2 paketas `picarx_control`
- sukurtas node `fusion_node`
- į node integruota:
  - ultragarso nuskaitymas
  - grayscale nuskaitymas
  - bazinė valdymo logika per `Picarx`

## 4. Svarbi pastaba
Šiame etape naudota line-follow logika buvo naudojama tik kaip:
- pirmas ROS2 integracijos testas
- jutiklių ir valdymo sujungimo patikra

Ji **nėra laikoma galutine roboto navigacijos strategija**.

Tolimesniuose etapuose:
- pagrindinei navigacijai bus naudojami lidar, odometrija, IMU, SLAM ir Nav2
- grayscale jutikliai bus laikomi pagalbiniais:
  - grindų ribos aptikimui
  - paviršiaus pokyčio aptikimui
  - docking / alignment pagalbai

## 5. Paleidimas
bash
sudo -E bash -c "source /opt/ros/jazzy/setup.bash && source /home/arvydas/ros2_ws/install/setup.bash && ros2 run picarx_control fusion_node"

## 6. Techninė realizacija

Node faile papildytas sys.path, kad ROS2 vykdymas pasiektų:

~/03_picarx_base_hw/.venv
~/vendor/picar-x
~/vendor/robot-hat

Tai buvo būtina, kad ros2 run aplinkoje būtų pasiekiamas Picarx.

## 7. Testavimo rezultatai
ROS2 paketas susibuildina
ros2 run veikia
node startuoja
Picarx importas veikia ROS aplinkoje
ultragarso jutiklio nuskaitymas veikia
grayscale jutiklių nuskaitymas veikia
bazinis valdymo ciklas veikia

## 8. Sukurti / naudoti failai
~/ros2_ws/src/picarx_control/picarx_control/fusion_node.py
~/ros2_ws/src/picarx_control/setup.py
stages/06_ros2_node/manifest.json
stages/06_ros2_node/README.md

## 9. Etapo rezultatas

Sukurtas pirmas veikiantis ROS2 node, kuris gali valdyti robotą ir skaityti jutiklius per Picarx.