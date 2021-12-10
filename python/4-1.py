#!/usr/local/bin/python3

def card_score(card):
    total = 0
    for row in card:
        for space in row:
            total += space
    return total

def is_winner(card):
    good_col = [ 1 for x in range(len(card[0]))]
    for row in card:
        winning = 1
        for i,space in enumerate(row):
            if space != 0:
                winning = 0
                good_col[i] = 0

        if winning:
            return card_score(card)
    if 1 in good_col:
        return card_score(card)
    return 0

def mark_value(card, value):
    for i,row in enumerate(card):
        for j,space in enumerate(row):
            if space == value:
                card[i][j] = 0
    return card

cards = []
card_id = -1
with open("4-1.input") as bingo:
    calls = [ int(call) for call in bingo.readline().split(',')]
    for i, line in enumerate(bingo):
        if line == "\n":
            if card_id != -1:
                cards.append(card)
            card = []
            card_id += 1
        else:
            card.append([ int(space) for space in line.split() ])
    cards.append(card)

for call in calls:
    for card in cards:
        mark_value(card, call)
        value = is_winner(card) * call
        if value:
            print(f"Winning card value is {value}")
            quit()
