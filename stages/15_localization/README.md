# Stage 15 – Localization using saved map

## Tikslas
Naudoti anksčiau išsaugotą žemėlapį lokalizacijai vietoje mapping režimo.

## Naudojami komponentai
- `nav2_map_server`
- `nav2_amcl`

## Naudojamas žemėlapis
- `/home/arvydas/14_map_save/maps/room_map.yaml`

## Įėjimai
- `/scan`
- `/odometry/filtered`
- TF:
  - `odom -> base_link`
  - `base_link -> laser`

## Išėjimai
- `/map`
- `/map_metadata`
- `/amcl_pose`
- `/particle_cloud`
- TF:
  - `map -> odom`

## Pasiekta
- `map_server` aktyvus
- `amcl` aktyvus
- publikuojami `/amcl_pose` ir `/particle_cloud`
- veikia transformacija `map -> odom`

## Pastabos
- šiame etape `slam_toolbox` mapping režimu nebenaudojamas
- lokalizacija atliekama pagal išsaugotą map
- AMCL inicializacijai gali reikėti `initialpose`

## Išvada
Stage 15 užbaigtas sėkmingai. Robotas lokalizuojasi pagal anksčiau išsaugotą žemėlapį.
