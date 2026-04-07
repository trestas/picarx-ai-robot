# Etapas 03 – PiCar-X bazinės aparatūros sužadinimas

## 1. Etapo paskirtis
Patikrinti ir užvesti PiCar-X bazinę aparatūrą: Robot HAT, vairo servo, kairįjį ir dešinįjį variklį, stabdymą ir trumpą rankinį judėjimą.

## 2. Ką turėjome etapo pradžioje
- Ubuntu Server 24.04.4 LTS
- ROS 2 Jazzy bazę
- Raspberry Pi 5 robote
- PiCar-X surinktą aparatinę platformą

## 3. Etapo tikslas
- Patikrinti bazinę aparatūros prieigą
- Užvesti vairo servo
- Užvesti kairįjį ir dešinįjį variklius
- Patikrinti stop funkciją
- Užfiksuoti pirmines kalibracijos reikšmes

## 4. Naudota aparatūra ir programinė įranga
- PiCar-X
- Raspberry Pi 5
- Robot HAT
- Ubuntu Server 24.04.4 LTS
- Python 3

## 5. Įgyvendinimo žingsniai
1. Sukurti etapo failus repo
2. Įdiegti bazines Python priklausomybes
3. Patikrinti Robot HAT / Python aplinką
4. Paleisti servo centro testą
5. Paleisti variklių testą
6. Paleisti trumpą judėjimo seką
7. Užfiksuoti rezultatus

## 6. Sukurti failai ir jų paskirtis
- `scripts/install_picarx_base.sh` – bazinių priklausomybių diegimas
- `scripts/check_hw_stack.sh` – aplinkos ir aparatūros sluoksnio patikra
- `scripts/deploy_stage3_to_pi.sh` – etapo failų nukėlimas į Raspberry Pi
- `scripts/collect_stage3_artifacts.sh` – rezultatų surinkimas
- `configs/picarx_base.env` – baziniai parametrų kintamieji
- `configs/calibration_template.yaml` – kalibracijos reikšmių šablonas
- `configs/safety_limits.yaml` – saugūs testiniai limitai
- `src/test_servo_center.py` – vairo servo testas
- `src/test_motors.py` – atskiras variklių testas
- `src/test_drive_sequence.py` – trumpa valdomo judėjimo seka
- `src/emergency_stop.py` – avarinio stabdymo komanda
- `artifacts/stage3-notes.txt` – faktiniai testų rezultatai

## 7. Testavimas
Bus tikrinama:
- ar veikia Python aparatūros sluoksnis
- ar servo gali būti centruojamas
- ar varikliai sukasi
- ar stop veikia
- ar trumpa judėjimo seka saugi
- ar kalibracijos duomenys užfiksuoti
- ar etapas išsaugotas GitHub

## 8. Galimi ribojimai / žinomos problemos
- Ubuntu aplinkoje gali tekti adaptuoti kai kurias SunFounder bibliotekų priklausomybes
- mechaninis vairo centras gali reikalauti kelių bandymų
- variklių kryptis gali būti priešinga nei tikėtasi

## 9. Etapo rezultatas
PiCar-X bazinis važiuoklės sluoksnis veikia ir yra paruoštas jutiklių etapams.

## 10. Ką šis etapas prideda bendram projektui
Sukuria bazę realiam roboto judėjimui, be kurios negalimas nei kliūčių vengimas, nei navigacija.

## 11. Kitas etapas
04 – Ultragarso jutiklio diegimas