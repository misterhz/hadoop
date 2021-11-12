#!/usr/bin/env python3

import sys

for line in sys.stdin:

    values = line.split(",")

    pedestrians_injured = values[11]
    pedestrians_killed = values[12]
    cyclists_injured = values[13]
    cyclist_killed = values[14]
    motorists_injured = values[15]
    motorist_killed = values[16]

    on_street = values[6]
    cross_street = values[7]
    off_street = values[8]

    try:
        year = int(values[0].split("/")[-1])
    except ValueError:
        continue  # no year available

    zip_code = values[2]

    if year <= 2012:
        continue

    if zip_code == "":
        continue

    for street in (on_street, cross_street, off_street):
        if street != "":
            print(f"{street}.{zip_code}.pedestrian.injured\t{pedestrians_injured}")
            print(f"{street}.{zip_code}.pedestrian.killed\t{pedestrians_killed}")
            print(f"{street}.{zip_code}.cyclist.injured\t{cyclists_injured}")
            print(f"{street}.{zip_code}.cyclist.killed\t{cyclist_killed}")
            print(f"{street}.{zip_code}.motorist.injured\t{motorists_injured}")
            print(f"{street}.{zip_code}.motorist.killed\t{motorist_killed}")


