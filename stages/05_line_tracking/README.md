# Etapas 05 – Line tracking + Sensor Fusion

## 1. Etapo paskirtis
Sukurti roboto gebėjimą:
- sekti liniją
- reaguoti į kliūtis
- sujungti kelis jutiklius į vieną elgesį

## 2. Ką turėjome pradžioje
- Veikiantį PiCar-X (03 etapas)
- Ultragarso jutiklį su safety stop (04 etapas)
- Stabilų Python runtime

## 3. Naudoti jutikliai

### Line sensor
python:
px.get_grayscale_data()

Grąžina:

[left, middle, right]
Ultragarso jutiklis
px.get_distance()

## 4. Logika

# Line tracking
jei centras mato liniją → važiuoti tiesiai
jei kairė stipresnė → sukti į kairę
jei dešinė stipresnė → sukti į dešinę
jei linija prarasta → stop
Safety
jei atstumas < 25 cm → stop

# Sensor fusion
JEI kliūtis → STOP
KITAIP → FOLLOW LINE

## 5. Naudoti parametrai
Parametras		Reikšmė
threshold		400
steering left	-15
steering right	15
forward speed	20
turn speed		18
safety distance	25 cm

## 6. Sukurti failai
src/line_read.py
src/line_follow.py
src/fusion_drive.py
configs/line_tracking.yaml
artifacts/stage5-notes.txt
manifest.json
README.md

## 7. Testavimo rezultatai
Line sensor: veikia
Line following: veikia
Ultrasonic stop: veikia
Fusion: veikia

# Robotas:
seka liniją
sustoja prie kliūties

## 8. Etapo rezultatas

Sukurtas pirmas autonominis elgesys:

navigacija pagal liniją
saugus sustojimas

Tai yra pagrindas:

pažangesniam sensor fusion
SLAM
ROS integracijai