############### Blackjack Project #####################
############### Our Blackjack House Rules #####################
## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
from art import logo

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackJack():
    while True:
        hit = True
        bust = False
        player = random.sample(cards, 2)
        computer = random.sample(cards, 2)

        # Player's turn
        while hit:
            print(f"You have {player} and the dealer has {computer[0]}")
            another_card = input("Do you want another card? 'y' or 'n': ")
            if another_card == 'y':
                player.append(random.choice(cards))
                if sum(player) > 21 and 11 in player:
                    player[player.index(11)] = 1
                if sum(player) > 21:
                    print(f"Bust, you lose! {player} {sum(player)}")
                    hit = False
                    bust = True
            else:
                hit = False

        if not bust:
            # Dealer's turn
            while sum(computer) < 17:
                computer.append(random.choice(cards))
            if 11 in computer and sum(computer) > 21:
                computer[computer.index(11)] = 1

            # Determine the winner
            player_total = sum(player)
            computer_total = sum(computer)
            print(f"You have {player_total} and the dealer has {computer_total}")
            if player_total > 21:
                print("You bust! Dealer wins.")
            elif computer_total > 21 or player_total > computer_total:
                print("You win!")
            elif player_total < computer_total:
                print("Dealer wins.")
            else:
                print("It's a tie!")

        play_again = input("Do you want to play again? 'y' or 'n': ")
        if play_again != 'y':
            print("Thanks for playing!")
            break

blackJack()
