#!/usr/local/bin/python3
period = 256 
gestation = 7
maturity = 2

iters = [ 0 for i in range(gestation) ]
babies = [ 0 for i in range(period) ]
total = 0

with open("6-1.input") as initial:
    ages = [ int(fish) for fish in initial.readline().split(',') ]
    for age in ages:
        total += 1
        iters[age] = iters[age] + 1
    
for day in range(period):
    iteration = day % gestation
    first_gen = day - (gestation + maturity)
    if first_gen > 0:
        iters[iteration] = iters[iteration] + babies[first_gen]
    babies[day] = iters[iteration]
    total += iters[iteration]

print(f"There are now {total} lanternfish to light your way to hell.")
