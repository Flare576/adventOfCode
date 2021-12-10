#!/usr/local/bin/python3

floor = []
cols = 0
def check_colums (new_cols):
    global cols, floor
    if new_cols > cols:
        cols = new_cols
        for row in floor:
            while len(row) <= cols: row.append(0)

def check_floor (rows):
    global cols, floor
    while len(floor) <= rows:
        floor.append([ 0 for x in range(cols + 1) ])

def count_unsafe ():
    unsafe = 0
    for row in floor:
        for space in row:
            if space > 1:
                unsafe += 1
    return unsafe

with open("5-1.input") as vents:
    for vent in vents:
        start, end = vent.split(" -> ")
        start = [ int(coord) for coord in start.split(",") ]
        end = [ int(coord) for coord in end.split(",") ]
        if start[0] == end[0]:
            near, far = sorted([start[1], end[1]])
            check_colums(start[0])
            check_floor(far)

            for row in floor[near:far+1]:
                row[start[0]] = row[start[0]] + 1
        elif start[1] == end[1]:
            near, far = sorted([start[0], end[0]])
            check_colums(far)
            check_floor(start[1])

            row = floor[start[1]]
            for i in range(near, far+1):
                row[i] = row[i] + 1
        else:
            check_colums(max(start[0],end[0]))
            check_floor(max(start[1],end[1]))
            dx = 1 if start[0] < end[0] else -1
            dy = 1 if start[1] < end[1] else -1
            x,y = start
            while x != end[0] + dx:
                floor[y][x] = floor[y][x] + 1
                x += dx
                y += dy

print(f"There are {count_unsafe()} unsafe spots.")
