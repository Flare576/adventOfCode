#!/usr/local/bin/python3
from numpy import loadtxt

previous = 0
deeper = 0
depths = loadtxt('1-1.input', dtype='int')
for window in range(len(depths)-2):
    current = sum(depths[window:window+3])
    if previous > 0 and current > previous:
        deeper += 1
    previous = current

print(f"It gets deeper {deeper} times")

