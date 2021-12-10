#!/usr/local/bin/python3

def find_it (candidates, find_oxy = True):
    position = 0
    while len(candidates) > 1:
        ones = []
        zeroes = []
        for line in candidates:
            if line[position] == "1":
                ones.append(line)
            else:
                zeroes.append(line)
        if find_oxy:
            if len(zeroes) > len(ones):
                candidates = zeroes
            else:
                candidates = ones
        else:
            if len(zeroes) <=len(ones):
                candidates = zeroes
            else:
                candidates = ones
        position += 1
            
    return candidates[0].strip()

size = 0

candidates = []
with open("3-1.input") as diagnostic:
    candidates = diagnostic.readlines()

oxy = find_it(candidates)
scrub = find_it(candidates, False)
oxyInt = int(oxy, 2)
scrubInt = int(scrub, 2)

print(f"Oxygen Generator Rating: {oxy}({oxyInt})\nCO2 Scrubber Rating: {scrub}({scrubInt})")
print(f"Life Support Rating: {oxyInt * scrubInt}")
