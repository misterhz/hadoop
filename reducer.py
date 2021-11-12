#!/usr/bin/env python3

import sys

current_key = None
current_count = 0

for line in sys.stdin:
    values = line.strip().split("\t")

    key = values[0].strip()
    count = int(values[1].strip())

    if current_key == key:
        current_count += count

    else:
        if current_key and current_count > 0:
            print("{}\t{}".format(current_key.replace('.', '\t'), current_count))

        current_key = key
        current_count = count

if current_key and current_count > 0:
    print("{}\t{}".format(current_key.replace('.', '\t'), current_count))
