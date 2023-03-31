from operator import truediv
import card, deck, player

starting_deck = deck.Deck()
player_one = player.Player(input("What is your name?"))
player_two = player.Player("COMPUTER")
game_on = True
war_is_on = False
def deal_cards():
    starting_deck.shuffle_deck()
    for x in range(26):
        player_one.add_cards(starting_deck.deal_card())
        player_two.add_cards(starting_deck.deal_card())
deal_cards()

print(player_one)
print(player_two)
round_num = 0
while game_on:
    if len(player_one.player_deck) == 0:
        print(f" {player_one.name} is out of cards, Player Two WINS!")
        game_on = False
        break
    if len(player_two.player_deck) == 0:
        print(f" The Computer is out of cards, Player Two WINS!")
        game_on = False
        break

    # new round start
    round_num += 1  
    print(f"Round {round_num}.... START!")

    player_one_cards, player_two_cards  = [], []
    player_one_cards.append(player_one.player_deck.pop())
    player_two_cards.append(player_two.player_deck.pop())

    print(f'{player_one.name} draws {player_one_cards[0].rank} of {player_one_cards[0].suit}')
    print(f'Computer draws {player_two_cards[0].rank} of {player_two_cards[0].suit}')
    if player_one_cards[0].value > player_two_cards[0].value:
        print(f"{player_one.name} wins!")
        player_one.add_cards(player_two_cards)
    elif player_two_cards[0].value > player_one_cards[0].value:
        print(f"Computer wins!")
        player_two.add_cards(player_one_cards)
    elif player_one_cards[0].value == player_two_cards[0].value:
        print("Both match, it's time for WAR!")
        war_is_on = True
        while war_is_on:
            player_one_cards.append(player_one.player_deck.pop())
            player_two_cards.append(player_two.player_deck.pop())
            player_one_cards.append(player_one.player_deck.pop())
            player_two_cards.append(player_two.player_deck.pop())
            player_one_cards.append(player_one.player_deck.pop())
            player_two_cards.append(player_two.player_deck.pop())
            # print("Both players drew 3 cards")
            # print(f'{player_one.name} draws {player_one_cards[-1].rank} of {player_one_cards[-1].suit}')
            # print(f'Computer draws {player_two_cards[-1].rank} of {player_two_cards[-1].suit}')
            print(f'{player_one.name} draws {player_one_cards[-1].rank} of {player_one_cards[-1].suit}')
            print(f'Computer draws {player_two_cards[-1].rank} of {player_two_cards[-1].suit}')
            if player_one_cards[-1].value > player_two_cards[-1].value:
                print(f"{player_one.name} wins!")
                player_one.add_cards(player_two_cards)
                war_is_on = False
                break
            elif player_two_cards[-1].value > player_one_cards[-1].value:
                print(f"Computer wins!")
                player_two.add_cards(player_one_cards)
                war_is_on = False
                break
            elif player_one_cards[-1].value == player_two_cards[-1].value:
                print("Both match, it's time for WAR!")
    print(player_one)
    print(player_two) 
    continue_playing = input("keep playing? Y/N")
    if continue_playing == "N":
        game_on = False
    

    

