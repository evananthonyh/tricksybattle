import random

# Deck set up
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
ranks = ["2","3","4","5","6","7","8","9","10", "Ace", "Jack", "Queen"]
values = {rank: i+1 for i, rank in enumerate(ranks)}

# Create and shuffle the deck
deck = [((suit, rank), values[rank]) for suit in suits for rank in ranks]
random.shuffle(deck)
