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


class CardCollection():
    def __init__(self, collection = []):
        self.collection = collection

    def __iter__(self):
        return iter(self.collection)

    def __getitem__(self, key):
        return self.collection[key]

    def __len__(self):
        return len(self.collection)

    def draw(self, index):
        self.index = index
        return self.collection.pop(self.index)

    def draw_from_top(self):
        return self.collection.pop(len(self.collection) - 1)

    def draw_from_botton(self):
        return self.collection.pop()

    def top_card(self):
        return self.collection[len(self.collection) - 1]

    def bottom_card(self):
        return self.collection[0]

    def add(self, card):
        self.card = card
        self.collection.append(self.card)

    def index(self, card):
        self.card = card
        return self.collection.index(self.card) if self.card in \
               self.collection else None


RANKS = {card: type(card, (Rank,), dict(symbol=card)) for card in RANK_CARDS}
SUITS = {suit: type(suit, (Suit,), dict(color=suit)) for suit in SUIT_CARDS}
