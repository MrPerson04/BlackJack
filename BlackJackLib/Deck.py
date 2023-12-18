from BlackJackLib.Card import Card
import random


class Deck:
    __slots__ = ['_contents', '_is_flipped', '_is_clickable']

    def __init__(self):
        self._contents = [Card("Hearts", "Ace"), Card("Hearts", "2"), Card("Hearts", "3"),
                          Card("Hearts", "4"), Card("Hearts", "5"), Card("Hearts", "6"),
                          Card("Hearts", "7"), Card("Hearts", "8"), Card("Hearts", "9"),
                          Card("Hearts", "10"), Card("Hearts", "Jack"), Card("Hearts", "Queen"),
                          Card("Hearts", "King"), Card("Diamonds", "Ace"), Card("Diamonds", "2"),
                          Card("Diamonds", "3"), Card("Diamonds", "4"), Card("Diamonds", "5"),
                          Card("Diamonds", "6"), Card("Diamonds", "7"), Card("Diamonds", "8"),
                          Card("Diamonds", "9"), Card("Diamonds", "10"), Card("Diamonds", "Jack"),
                          Card("Diamonds", "Queen"), Card("Diamonds", "King"), Card("Clubs", "Ace"),
                          Card("Clubs", "2"), Card("Clubs", "3"), Card("Clubs", "4"),
                          Card("Clubs", "5"), Card("Clubs", "6"), Card("Clubs", "7"),
                          Card("Clubs", "8"), Card("Clubs", "9"), Card("Clubs", "10"),
                          Card("Clubs", "Jack"), Card("Clubs", "Queen"), Card("Clubs", "King"),
                          Card("Spades", "Ace"), Card("Spades", "2"), Card("Spades", "3"),
                          Card("Spades", "4"), Card("Spades", "5"), Card("Spades", "6"),
                          Card("Spades", "7"), Card("Spades", "8"), Card("Spades", "9"),
                          Card("Spades", "10"), Card("Spades", "Jack"), Card("Spades", "Queen"),
                          Card("Spades", "King")]
        self._is_flipped = False
        self._is_clickable = True

    def __str__(self):
        ret_array = ""
        for cards in self._contents:
            ret_array += str(cards) + ", "
        return ret_array

    def shuffle(self):
        random.shuffle(self._contents)

    def pop(self):
        return self._contents.pop()

    def is_flipped(self):
        return self._is_flipped

    def set_flipped(self, flipped: bool):
        self._is_flipped = flipped

    def is_clickable(self):
        return self._is_clickable

    def set_clickable(self, clickable: bool):
        self._is_clickable = clickable
