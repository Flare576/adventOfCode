#!/usr/local/bin/python3

x = 0
y = 0
aim = 0
with open("2-1.input") as course:
    for line in course:
        direction, size = line.split()
        if direction == 'forward':
            x += int(size)
            y += int(size) * aim
        elif direction == 'up':
            aim -= int(size)
        elif direction == 'down':
            aim += int(size)
print(f"You've gone {x} forward and {y} deep, or {x*y}")
