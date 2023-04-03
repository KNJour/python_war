import card, deck

class Player:
    def __init__(self, name):
        self.name = name
        self.player_deck = []

    def play_card(self):
        return self.player_deck.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.player_deck.extend(new_cards)
        else:
            self.player_deck.append(new_cards)
    def __str__(self):
        return f'Player {self.name} has {len(self.player_deck)} cards'


