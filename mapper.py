#!/usr/bin/env python3

import sys

skip = False

for line in sys.stdin:

    if not skip:
        skip = True
        continue

    values = line.split(",")

    pedestrians_injured = values[11]
    pedestrians_killed = values[12]
    cyclist_injured = values[13]
    cyclist_killed = values[14]
    motorist_injured = values[15]
    motorist_killed = values[16]

    on_street = values[6]
    cross_street = values[7]
    off_street = values[8]

    year = int(values[0].split("/")[2])
    zip_code = values[2]

    if year <= 2012:
        continue

    if zip_code == "":
        continue

    for street in (on_street, cross_street, off_street):
        if street != "":
            print(f"{street}\t{zip_code}\tpedestrians\tinjured\t{pedestrians_injured}")
            print(f"{street}\t{zip_code}\tpedestrians\tkilled\t{pedestrians_killed}")
            print(f"{street}\t{zip_code}\tcyclist\tinjured\t{cyclist_injured}")
            print(f"{street}\t{zip_code}\tcyclist\tkilled\t{cyclist_killed}")
            print(f"{street}\t{zip_code}\tmotorist\tinjured\t{motorist_injured}")
            print(f"{street}\t{zip_code}\tmotorist\tkilled\t{motorist_killed}")


