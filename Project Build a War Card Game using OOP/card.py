from suit import Suit
class Card:

    SPECIAL_CARDS_VALUES_TO_DESCRIPTIONS = {11 : "Jack", 12 : "Queen", "13" : "King", "14" : "Ace"}

    def __init__(self, suit: Suit, value):
        self._suit = suit
        self._value = value

    @property
    def suit(self):
        return self._suit

    @property
    def value(self):
        return self._value

    def show(self):
        if self.is_special():
            print(f"{Card.SPECIAL_CARDS_VALUES_TO_DESCRIPTIONS[self.value]} of {self.suit} {self._suit.symbol}")
        else:
            print(f"{self.value} of {self.suit} {self.suit.symbol}")

    def is_special(self):
        if self.value >= 11:
            return True

        else:
            return False