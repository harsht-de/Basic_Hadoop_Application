#!/usr/bin/env python3
import sys

# --------- Mapper ---------
def mapper():
    for line in sys.stdin:
        if line.startswith("age"):
            continue
        fields = line.strip().split(",")
        if len(fields) < 5:
            continue
        age = int(fields[0])
        chol = int(fields[4])
        age_group = f"{(age//10)*10}-{(age//10)*10+9}"  # 30–39, 40–49...
        print(f"{age_group}\t{chol},1")

# --------- Reducer ---------
def reducer():
    current_key = None
    chol_sum = 0
    count = 0
    for line in sys.stdin:
        key, value = line.strip().split("\t")
        chol, cnt = value.split(",")
        chol, cnt = int(chol), int(cnt)

        if current_key == key:
            chol_sum += chol
            count += cnt
        else:
            if current_key:
                print(f"{current_key}\t{chol_sum/count:.2f}")
            current_key = key
            chol_sum = chol
            count = cnt

    if current_key:
        print(f"{current_key}\t{chol_sum/count:.2f}")

# --------- Run Hadoop mode ---------
if __name__ == "__main__":
    if sys.argv[1] == "mapper":
        mapper()
    elif sys.argv[1] == "reducer":
        reducer()
