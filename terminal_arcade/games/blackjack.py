import random
from utils import title


def play():

    title("BLACKJACK")

    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]*4
    random.shuffle(deck)

    player = [deck.pop(), deck.pop()]

    print("\n🎰 Dealer starting...")

    while True:

        print(f"\n📊 Your cards: {player}")
        print(f"   Total: {sum(player)}")

        if sum(player) > 21:
            print("\n❌ Bust! You went over 21. You lose!")
            return

        while True:
            move = input("\n(h)it or (s)tand? ").lower().strip()
            if move in ["h", "s"]:
                break
            print("❌ Please enter 'h' to hit or 's' to stand.")

        if move == "h":
            player.append(deck.pop())
            print("Dealer gave you a card...")
        else:
            break

    dealer = [deck.pop(), deck.pop()]
    print(f"\n🎯 Dealer reveals: {dealer}")

    while sum(dealer) < 17:
        dealer.append(deck.pop())
        print("Dealer draws another card...")

    print(f"Dealer's final hand: {dealer} (Total: {sum(dealer)})")

    if sum(dealer) > 21:
        print("\n✅ Dealer busted! You win!")
    elif sum(player) > sum(dealer):
        print("\n✅ You win!")
    else:
        print("\n❌ Dealer wins!")
