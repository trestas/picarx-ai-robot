# Stage 16 – Navigation base

## Tikslas
Integruoti Nav2 bazę su PiCar-X ir prijungti navigacijos greičio komandas prie realaus roboto valdymo.

## Pasiekta
- paleistas Nav2 stack
- aktyvūs pagrindiniai navigacijos mazgai
- veikia `/navigate_to_pose`
- sukurtas `cmd_vel_bridge_node`
- rankinis `/cmd_vel_smoothed` testas sėkmingai judina robotą

## Naudojami komponentai
- `nav2_bringup`
- `nav2_map_server`
- `nav2_amcl`
- `nav2_controller`
- `nav2_planner`
- `nav2_bt_navigator`
- `nav2_velocity_smoother`
- custom `cmd_vel_bridge_node`

## Architektūra
- Nav2 generuoja navigacijos komandas
- Nav2 išėjimas naudojamas per `/cmd_vel_smoothed`
- `cmd_vel_bridge_node` konvertuoja Twist komandas į PiCar-X valdymą

## Patvirtinta
- action serveriai egzistuoja:
  - `/navigate_to_pose`
  - `/navigate_through_poses`
- controlleris bando vykdyti kelią
- robotas reaguoja į rankines Twist komandas

## Dabartinis ribojimas
`navigate_to_pose` neužbaigia tikslo, nes controlleris meta `Failed to make progress`.

## Root cause
Trūksta patikimos translacinės odometrijos (x/y). Dabartinė sistema turi nepakankamą judėjimo progreso atspindėjimą localization / odom grandinėje.

## Išvada
Stage 16 užbaigtas kaip Nav2 bazės integracijos etapas. Stage 17 tikslas – išspręsti judėjimo progreso / odometrijos problemą.
