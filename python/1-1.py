#!/usr/local/bin/python3

previous = 0
deeper = 0
with open("1-1.input") as depths:
    for depth in depths:
        depth = int(depth)
        if previous > 0 and depth > previous:
            deeper += 1

        previous = depth

print(f"It gets deeper {deeper} times")

