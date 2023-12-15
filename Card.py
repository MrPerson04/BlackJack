class Card:
    def __init__(self, s, v):
        self._suit = s
        self._value = v

    def __str__(self):
        return self._value + " of " + self._suit

    def get_suit(self):
        return self._suit

    def get_value(self):
        if self._value == "Ace":
            # return 11 which will be checked by hand to apply ace rules
            return 11
        elif self._value == "King" or self._value == "Queen" or self._value == "Jack":
            return 10
        else:
            return int(self._value)
