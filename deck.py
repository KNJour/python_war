import random
import card

class Deck:
    def __init__(self):
        # creates an empty list of cards
        self.all_cards = []
        # loops through the suits variable and ranks variable. for each instance of suit it creates one rank, completing the deck. variables located in the card class as global variables
        for suit in card.suits:
            for rank in card.ranks:
                new_card = card.Card(rank, suit)
                self.all_cards.append(new_card)
    
    # shuffles the list of cards in self.all_cards
    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def deal_card(self):
        # returns one card from the 
        return self.all_cards.pop()
