#!/usr/local/bin/python3
from math import floor, factorial
from statistics import mean, median, mode

crabs = []
def gas (target):
    global crabs
    return sum([ (abs(target - pos)) for pos in crabs ])

with open("7-1.input") as initial:
    crabs = [ int(crab) for crab in initial.readline().split(',') ]

mdn = floor(median(crabs)), gas(floor(median(crabs)))

print(f"Crabs should converge on Median position: {mdn[0]}, costing {mdn[1]} gas.") 
