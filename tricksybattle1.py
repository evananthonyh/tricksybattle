import random

# Deck set up
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
ranks = ["2","3","4","5","6","7","8","9","10", "Ace", "Jack", "Queen"]
values = {rank: i+1 for i, rank in enumerate(ranks)}

# Create and shuffle the deck
deck = [((suit, rank), values[rank]) for suit in suits for rank in ranks]
random.shuffle(deck)

# Deal 8 cards to each player
player1 = deck[:8]
player2 = deck[8:16]
deck = deck[16:]

# Start scores at 0
player1_score = 0
player2_score = 0

# Play 8 rounds
for round_num in range(1, 9):
    print(f"\nRound {round_num}")

    # Player 1 starts
    card_a = player1.pop()
    card_b = player2.pop()

    # Card descriptions
    card_a_str = f"{card_a[0][1]} of {card_a[0][0]}"
    card_b_str = f"{card_b[0][1]} of {card_b[0][0]}"
    print(f"Card A is a {card_a_str}")
    print(f"Card B is a {card_b_str}")

# Determine winner
    if card_a[0][0] == card_b[0][0]:  # Same suit
        if card_a[1] > card_b[1]:
            print(f"{card_a_str} beats {card_b_str}, Player 1 wins the round!")
            player1_score += 1
        elif card_b[1] > card_a[1]:
            print(f"{card_b_str} beats {card_a_str}, Player 2 wins the round!")
            player2_score += 1
        else:
            print("It's a tie!")
    else:
        print(f"Different suits, Player 1 wins the round!")
        player1_score += 1
