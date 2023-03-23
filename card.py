from symbol import subscriptlist
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {
    'Two': 2,
    'Three': 3,
    'Four' : 4,
    'Five' : 5,
    'Six' : 6,
    'Seven' : 7,
    'Eight' : 8,
    'Nine' : 9,
    'Ten' : 10,
    'Jack' : 11,
    'Queen' : 12,
    'King' : 13,
    'Ace' : 14
}

class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit
    
three_of_clubs = Card("Three", "Clubs")
two_hearts = Card("Two", "Hearts")
print(two_hearts.value < three_of_clubs.value)
