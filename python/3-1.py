#!/usr/local/bin/python3

ones = []
size = 0
with open("3-1.input") as diagnostic:
    for line in diagnostic:
        size += 1
        for i, digit in enumerate(line):
            if "\n" == digit:
                continue
            if len(ones) == i:
                ones.append(0)
            if digit == "1":
                ones[i] = ones[i] + 1
print(size, ones)

gamma = ''
eps = ''
for count in ones:
    if count > size/2:
        gamma += "1"
        eps += "0"
    else:
        gamma += "0"
        eps += "1"

gammaInt = int(gamma, 2)
epsInt = int(eps, 2)
print(f"Gamma: {gamma}({gammaInt})\nEpsilon: {eps}({epsInt})")
print(f"Power: {gammaInt * epsInt}")
