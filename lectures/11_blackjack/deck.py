from random import shuffle
from itertools import product

Faces = [str(face) for face in range(2, 11)] + ['J', 'Q', 'K', 'A']

Suits = ['C', 'D', 'H', 'S']


class Card:

    def __init__(self, face, suit):
        self.face = face
        self.suit = suit
        self.value = self.calc_value()

    def __str__(self):
        return self.face + self.suit

    def __repr__(self):
        return str(self)

    def calc_value(self):
        if self.face in [str(i) for i in range(2, 11)]:
            return int(self.face)
        elif self.face == "A":
            return 11
        else:
            return 10


class Deck:

    def __init__(self):
        self.cards = [Card(face, suit)
                      for (face, suit) in product(Faces, Suits)]

    def __str__(self):
        output = []
        for card in self.cards:
            output.append(str(card))
        return ' '.join(output)

    def random(self):
        shuffle(self.cards)
