class Suit:

    DESCRIPTION_TO_SYMBOL = {"club" : "♣", "diamond" : "♦", "heart" : "♥", "spade" : "♠"}

    def __init__(self, description, symbol):
        self._description = description
        self._symbol = symbol

    @property
    def description(self):
        return self._description

    @property
    def symbol(self):
        return self._symbol

