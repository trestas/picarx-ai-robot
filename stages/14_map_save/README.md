# Stage 14 – Map Save

## Tikslas
Išsaugoti SLAM sugeneruotą žemėlapį į failus, kad jis galėtų būti naudojamas lokalizacijai ir vėlesnei navigacijai.

## Naudotas įrankis
- `nav2_map_server`
- `map_saver_cli`

## Sukurti failai
- `maps/room_map.pgm`
- `maps/room_map.yaml`

## Reikalingos veikiančios dalys prieš saugojimą
- `/scan`
- `/map`
- `slam_toolbox`
- TF grandinė:
  - `map -> odom`
  - `odom -> base_link`
  - `base_link -> laser`

## Paleidimo komanda
	ros2 run nav2_map_server map_saver_cli -f /home/arvydas/14_map_save/maps/room_map
## Rezultatas

Sukurtas pakartotinai naudojamas žemėlapis lokalizacijos režimui.
