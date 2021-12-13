#!/usr/local/bin/python3

with open("6-1.input") as initial:
    ages = [ int(fish) for fish in initial.readline().split(',') ]

for day in range(80):
    for i, fish in enumerate(ages):
        if fish == 0:
            ages[i] = 6
            ages.append(9)
        else:
            ages[i] = fish -1

print(f"There are now {len(ages)} lantern fish, and goat help you")

