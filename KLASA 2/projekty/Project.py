import random

letters = ['2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A']
symbols = ["♥", "♦", "♠", "♣"]

cards = [letter + symbol for symbol in symbols for letter in letters]
random.shuffle(cards)

player1 = []
player2 = []
player3 = []
player4 = []
table = []

# Rozdanie kart graczom
for x in range(2):
    player1.append(cards.pop())
    player2.append(cards.pop())
    player3.append(cards.pop())
    player4.append(cards.pop())

# Karty na stół
def deal_community_cards(table, cards, amount):
    for i in range(amount):
        table.append(cards.pop())

# Opcje ruchu
def check:
def call:
def bet:
def fold:
# FLOP
deal_community_cards(table, cards, 3)
print(f'FLOP: {table}')

#Pierwsze decyzje

#TURN
deal_community_cards(table, cards, 1)
print(f'TURN: {table}')

#drugie decyzje

#RIVER
deal_community_cards(table, cards, 1)
print(f'RIVER: {table}')

#ostatnie decyzje