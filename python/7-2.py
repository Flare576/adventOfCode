#!/usr/local/bin/python3
from math import floor, factorial, ceil
from statistics import mean, median, mode

crabs = []
def gas (target):
    global crabs
    total = 0
    for pos in crabs:
        base = abs(target - pos)
        cost = (base * (base + 1)) / 2
        total += cost
    return total

with open("7-1.test") as initial:
    crabs = [ int(crab) for crab in initial.readline().split(',') ]

mn = ceil(mean(crabs)), gas(ceil(mean(crabs)))
mdn = ceil(median(crabs)), gas(ceil(median(crabs)))
md = ceil(mode(crabs)), gas(ceil(mode(crabs)))

print( mn, mdn, md)
# print(f"Crabs should converge on Mean position: {mn[0]}, costing {mn[1]} gas.") 
