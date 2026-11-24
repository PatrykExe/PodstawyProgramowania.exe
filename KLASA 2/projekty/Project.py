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

def deal_community_cards(table, cards, amount):
    for i in range(amount):
        table.append(cards.pop())

deal_community_cards(table, cards, 3)  # Flop
deal_community_cards(table, cards, 1)  # Turn
deal_community_cards(table, cards, 1)  # River
