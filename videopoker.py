import random


def create_deck():
    ranks_all = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    suits_all = ['hearts', 'diamonds', 'clubs', 'spades']
    return [(rank, suit) for rank in ranks_all for suit in suits_all]


def draw_hand(deck):
    return random.sample(deck, 5)


def evaluate_hand(hand, bet):
    ranks = [rank for rank, suit in hand]
    suits = [suit for rank, suit in hand]

    # For straight evaluation
    rank_map = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                'jack': 11, 'queen': 12, 'king': 13, 'ace': 14}
    rank_values = sorted([rank_map[rank] for rank in ranks])

    # For flush, full house, three of a kind, two pair, one pair evaluation
    rank_counts = {rank: ranks.count(rank) for rank in set(ranks)}
    suit_counts = {suit: suits.count(suit) for suit in set(suits)}

    is_flush = max(suit_counts.values()) == 5
    is_straight = all(rank_values[i] + 1 == rank_values[i + 1] for i in range(len(rank_values) - 1))
    if not is_straight and 'ace' in ranks:
        rank_values = sorted([1 if rank == 'ace' else rank_map[rank] for rank in ranks])
        is_straight = all(rank_values[i] + 1 == rank_values[i + 1] for i in range(len(rank_values) - 1))

    if is_flush and is_straight:
        return bet * 50, "Straight Flush!"
    elif 3 in rank_counts.values() and 2 in rank_counts.values():
        return bet * 25, "Full House!"
    elif is_flush:
        return bet * 20, "Flush!"
    elif is_straight:
        return bet * 15, "Straight!"
    elif max(rank_counts.values()) == 3:
        return bet * 10, "Three of a kind!"
    elif list(rank_counts.values()).count(2) == 2:
        return -bet, "Two Pair"
    elif max(rank_counts.values()) == 2:
        return -bet * 2, "One Pair"
    else:
        return -bet * 3, "High Card"


def video_poker(bet):
    deck = create_deck()
    hand = draw_hand(deck)
    print("Your hand:", hand)
    points, message = evaluate_hand(hand, bet)
    print(f"{message} Points for this hand: {points}")
    return points


def play_game():
    total_earnings = 0
    rounds_played = 0

    while rounds_played < 300 and -200 < total_earnings < 100:
        if rounds_played == 0:
            try:
                print("Welkom bij TTK casino, Amsterdam! You can play no more than 300 rounds. And if you lose more ")
                print("than 200 euros or earn more than 100 euros, either way you must leave.")
                input("Press Enter to enter the casino...")
                bet = int(input("Place your bet (1 Euro): "))
                if bet != 1:
                    print("Invalid bet. You must bet exactly 1 Euro.")
                    continue
            except ValueError:
                print("Please enter a valid number for your bet.")
                continue
        else:
            try:
                bet = int(input("Place your bet: "))
            except ValueError:
                print("Please enter a valid number for your bet.")
                continue

        result = video_poker(bet)
        total_earnings += result
        rounds_played += 1

        print(f"Round {rounds_played}: {result} Euro(s). Total earnings: {total_earnings} Euro(s).")

        if total_earnings >= 100:
            print("Congratulations! You've won (more than) 100 Euros!")
            break
        elif total_earnings <= -200:
            print("Game over! You've lost (more than) 200 Euros.")
            break

    print("Game finished. Total earnings:", total_earnings, "Euro(s) after", rounds_played, "rounds.")


play_game()
