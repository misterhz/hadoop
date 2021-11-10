#!/usr/bin/env python3

import sys

current_street = None
current_zip_code = None
current_damage = None
current_type = None
current_count = 0

for line in sys.stdin:
    values = line.strip().split("\t")

    street = values[0].strip()
    zip_code = values[1].strip()
    human_type = values[2].strip()
    damage = values[3].strip()
    count = int(values[4].strip())

    if current_damage == damage and \
            current_zip_code == zip_code and \
            current_type == human_type and \
            current_street == street:  # is different damage enough?
        current_count += count

    else:
        if current_damage and current_count > 0:
            print(f"{current_street}\t{current_zip_code}\t{current_type}\t{current_damage}\t{current_count}")

        current_street = street
        current_zip_code = zip_code
        current_type = human_type
        current_damage = damage
        current_count = count

if current_damage and current_count > 0:
    print(f"{current_street}\t{current_zip_code}\t{current_type}\t{current_damage}\t{current_count}")
