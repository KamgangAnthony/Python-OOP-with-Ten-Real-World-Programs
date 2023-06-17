import random
from suit import Suit
from card import Card


class Deck:

    def __init__(self, is_empty = False):
        self._cards = []

        if not is_empty:
            self.build()

    @property
    def size(self):
        return len(self.cards)

    @property
    def cards(self):
        return self._cards

    def build(self):
        for suit in Suit.DESCRIPTION_TO_SYMBOL:
            for value in range(2, 15):
                self.cards.append(Card(Suit(suit, Suit.DESCRIPTION_TO_SYMBOL[suit]), value))

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if self.cards:
            return self.cards.pop()
        else:
            return None

    def add(self, card: Card):
        self.cards.insert(0, card)

