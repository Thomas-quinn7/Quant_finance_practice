import collections
from operator import __add__
import random
import math
Card = collections.namedtuple('Card', ['rank', 'suit'])
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
            for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()    
len(deck)
from random import choice
print(choice(deck))

for card in reversed(deck):
    print(card)

suit_values = dict(spades=3, hearts=2,diamonds=1,clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)



class Vector:
    def __init__ (self,x=0,y=0):
        self.x=x
        self.y=y

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'
    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self,other):
        x= self.x + other.x
        y= self.y + other.y
        return Vector(x,y)

    def __mul__(self,Scalar):
        return Vector(self.x*Scalar,self.y*Scalar)
    
colours=['Black','White']
sizes=['S','M','L']
tshirts=[(colour,size)for colour in colours for size in sizes]
print(tshirts)


