#!/usr/bin/env python3
import sys

# --------- Mapper ---------
def mapper():
    for line in sys.stdin:
        if line.startswith("age"):  # skip header
            continue
        fields = line.strip().split(",")
        if len(fields) < 2:
            continue
        sex = fields[1]   # 1 = Male, 0 = Female
        print(f"{sex}\t1")

# --------- Reducer ---------
def reducer():
    current_key = None
    total = 0
    for line in sys.stdin:
        key, value = line.strip().split("\t")
        value = int(value)

        if current_key == key:
            total += value
        else:
            if current_key:
                print(f"{current_key}\t{total}")
            current_key = key
            total = value

    if current_key:
        print(f"{current_key}\t{total}")

# --------- Run Hadoop mode ---------
if __name__ == "__main__":
    if sys.argv[1] == "mapper":
        mapper()
    elif sys.argv[1] == "reducer":
        reducer()
