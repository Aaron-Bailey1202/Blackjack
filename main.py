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
    hit = True
    bust = False
    player = random.sample(cards, 2)
    computer = random.sample(cards, 2)

    # while hit is true the player will choose whether to have another card or not, once the player either is finished they can pick 'n'
    while hit:
        print(f"You have {player} and the dealer has {computer[0]}")
        another_card = input("Do you want another card? 'y' or 'n':")
        if another_card == 'y':
            player.append(random.choice(cards))
            # if there is an ace(11) and the player is over 21 the 11 is converted to a 1
            while sum(player) > 21 and 11 in player:
                target_index = player.index(11)
                player[target_index] = 1
            if sum(player) > 21:
                print(f"Bust, you lose! {player} {sum(player)}")
                hit = False
                bust = True
        else:
            hit = False
    # if hit is false or the player has not gone bust (over 21) then this will run until the computer has gone above 17
    if not bust:
        while sum(computer) < 17:
            computer.append(random.choice(cards))
        if sum(player) > 21 and 11 in player:
            target_index = computer.index(11)
            computer[target_index] = 1
        if sum(computer) > 21:
            print(f"You have {sum(player)} and the dealer has {sum(computer)} you win!")
        else:
            print(f"You have {sum(player)} and the dealer has {sum(computer)} you lose!")

    play_again = input("Do you want to play again? 'y' or 'n'")
    if play_again == 'y':
        blackJack()


blackJack()