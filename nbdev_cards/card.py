"""A simple API for creating and using playing cards."""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_card.ipynb.

# %% auto 0
__all__ = ['suits', 'ranks', 'Card']

# %% ../nbs/00_card.ipynb 3
suits = ['♣️','♦️','♥️','♠️']

# %% ../nbs/00_card.ipynb 9
ranks = [None, "A"] + [str(x) for x in range(2, 11)] + ["J", "Q", "K"]

# %% ../nbs/00_card.ipynb 13
class Card:
    "A playing card."
    def __init__(self,
                 suit: int, # An index into the `suits`
                 rank: int):  # An index into the `ranks`
        
        self.suit = suit
        self.rank = rank

        
    def __repr__(self):
        return f"{ranks[self.rank]}{suits[self.suit]}"
    
    def __eq__(self, value):
        return self.suit == value.suit and self.rank == value.rank
    

# %% ../nbs/00_card.ipynb 20
from fastcore.utils import patch

# %% ../nbs/00_card.ipynb 21
@patch
def __lt__(self:Card,
           other:Card): 
    return self.suit < other.suit and self.rank < other.rank

# %% ../nbs/00_card.ipynb 22
@patch
def __gt__(self:Card, other:Card):
    return self.suit > other.suit and self.rank > other.rank
