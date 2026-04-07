# Etapas 04 – Ultragarso jutiklis (Obstacle Detection + Safety Layer)

## 1. Etapo paskirtis
Integruoti ultragarso jutiklį ir sukurti pirmą realų saugos sluoksnį robote.

## 2. Ką turėjome etapo pradžioje
- Veikiantį PiCar-X (03 etapas)
- Python valdymą per Picarx klasę
- Paruoštą .venv aplinką

## 3. Problema
Bandymas naudoti:
- RPi.GPIO
- gpiozero + rankinius BCM pin'us

neveikė Raspberry Pi 5 aplinkoje:
- klaida: `Cannot determine SOC peripheral base address`
- neteisingi TRIG/ECHO pin'ai

## 4. Galutinis sprendimas
Naudotas integruotas PiCar-X driveris:

```python
px.get_distance()