"""A deck of playing cards"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_deck.ipynb.

# %% auto 0
__all__ = ['Deck', 'draw_n']

# %% ../nbs/01_deck.ipynb 3
from .card import * 
from fastcore.utils import patch
from fastcore.test import *

# %% ../nbs/01_deck.ipynb 4
class Deck:
    "A deck of cards" 
    def __init__(self): 
        self.cards = [Card(suit, rank) for suit in range(4) for rank in range(1,14)]

    def __repr__(self):
        return '; '.join(map(str, self.cards))
    
    def __len__(self):
        return len(self.cards)
    
    def __contains__(self, card):
        return card in self.cards
    

    def shuffle(self):
        "Shuffle the deck"
        return random.shuffle(self.cards)
    
    __str__ = __repr__

# %% ../nbs/01_deck.ipynb 11
@patch
def pop(self: Deck, 
        i=-1): # The index of the card to remove (default is the last card)
    "Remove and return the card at index `i`"
    return self.cards.pop(i)    

# %% ../nbs/01_deck.ipynb 19
def draw_n(n: int, # number of cards to draw
           replace: bool = False # whether to replace the cards drawn
           ):
    "Draw `n` cards from the deck"
    d = Deck()
    d.shuffle()
    if replace:
        return [d.cards[random.choice(range(len(d.cards)))] for _ in range(n)]
    else:
        return d.cards[:n]
