#!/usr/bin/env python3

RANK_CARDS = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
              'Nine', 'Ten', 'Jack', 'Queen', 'King']
SUIT_CARDS = ['Hearts', 'Clubs', 'Spades', 'Diamonds']


class Rank(object):
    symbol = None

    def __eq__(self, other):
        return self.symbol == other.symbol

    def __str__(self):
        return str(self.symbol)


class Suit(object):
    color = None

    def __eq__(self, other):
        return self.color == other.color

    def __str__(self):
        return str(self.color)

class Card():
    def __init__(self, rank, suit):
        self.rank = rank()
        self.suit = suit()

    def __str__(self):
        return str(self.rank) + ' of ' + str(self.suit)

    def __setattr__(self, rank, suit):
        if not 'rank' in self.__dict__ or not 'suit' in self.__dict__:
            return object.__setattr__(self, rank, suit)
        else:
            raise AttributeError("Can't set attribute")

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit


#class CardCollection():


RANKS = {card: type(card, (Rank,), dict(symbol=card)) for card in RANK_CARDS}
SUITS = {suit: type(suit, (Suit,), dict(color=suit)) for suit in SUIT_CARDS}
