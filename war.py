from operator import truediv
import card, deck, player

# Game start, great a starting deck and 2 players. prompts player 1 for input. sets variables for whether "war" is occurring, and if the game is to continue. 
starting_deck = deck.Deck()
player_one = player.Player(input("What is your name?"))
player_two = player.Player("COMPUTER")
game_on = True
war_is_on = False
# shuffles the deck of cards and distributes them between the player and the computer. round variable is created to keep track of round #, and an empty list is created for the players in field cards
def deal_cards():
    starting_deck.shuffle_deck()
    for x in range(26):
        player_one.add_cards(starting_deck.deal_card())
        player_two.add_cards(starting_deck.deal_card())
deal_cards()
print(player_one)
print(player_two)
player_one_cards = list()
player_two_cards = list()
round_num = 0
# game runs on a while loop, which ends if either player is out of cards, or if you choose to end it at the end of a round
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
    player_one_cards.clear()
    player_two_cards.clear()
    print(player_one_cards)
    print(player_two_cards)
    player_one_cards.append(player_one.play_card())
    player_two_cards.append(player_two.play_card())
    print(player_one_cards[0].rank)
    print(player_two_cards[0].rank)
    print(f'{player_one.name} draws {player_one_cards[0].rank} of {player_one_cards[0].suit}')
    print(f'Computer draws {player_two_cards[0].rank} of {player_two_cards[0].suit}')
    # Checks to see if who has the higher value. if values are the same, WAR is started
    if player_one_cards[-1].value > player_two_cards[-1].value:
        print(f"{player_one.name} wins!")
        player_one_cards.extend(player_two_cards)
        player_one.add_cards(player_one_cards)
        
    elif player_two_cards[-1].value > player_one_cards[-1].value:
        print(f"Computer wins!")
        player_two_cards.extend(player_one_cards)
        player_two.add_cards(player_two_cards)
        
    elif player_one_cards[-1].value == player_two_cards[-1].value:
        print("Both match, it's time for WAR!")
        war_is_on = True
        while war_is_on:
            # When war is started, checks to see if players have enough cards for war. if one does not, they lose
            if len(player_one.player_deck) < 5:
                print(f" {player_one.name} does not have enough cards for WAR, Player Two WINS!")
                game_on = False
                break
            if len(player_two.player_deck) < 5:
                print(f" does not have enough cards for WAR, Player Two WINS!")
                game_on = False
                break
            # WAR is on, each player draws 5 cards, the last card drawn by each player is evaluated for who wins, if no one wins, the while loop continues and more cards are drawn
            player_one_cards.append(player_one.player_deck.pop())
            player_two_cards.append(player_two.player_deck.pop())
            player_one_cards.append(player_one.player_deck.pop())
            player_two_cards.append(player_two.player_deck.pop())
            player_one_cards.append(player_one.player_deck.pop())
            player_two_cards.append(player_two.player_deck.pop())
            player_one_cards.append(player_one.player_deck.pop())
            player_two_cards.append(player_two.player_deck.pop())
            player_one_cards.append(player_one.player_deck.pop())
            player_two_cards.append(player_two.player_deck.pop())

            print(f'{player_one.name} draws 5 Cards, the last is a {player_one_cards[-1].rank} of {player_one_cards[-1].suit}')
            print(f'Computer draws 5 Cards, the last is a {player_two_cards[-1].rank} of {player_two_cards[-1].suit}')
            if player_one_cards[-1].value > player_two_cards[-1].value:
                print(f"{player_one.name} wins!")
                player_one_cards.extend(player_two_cards)
                player_one.add_cards(player_one_cards)
                war_is_on = False
                break
            elif player_two_cards[-1].value > player_one_cards[-1].value:
                print(f"Computer wins!")
                player_two_cards.extend(player_one_cards)
                player_two.add_cards(player_two_cards)
                war_is_on = False
                break
            elif player_one_cards[-1].value == player_two_cards[-1].value:
                print("Both match, it's time for WAR!")
    print(player_one)
    print(player_two) 
    continue_playing = input("keep playing? Y/N")
    if continue_playing == "N":
        game_on = False
    

    

