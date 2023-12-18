from Deck import Deck

class Hand:
    def __init__(self, deck: Deck):
        self._contents = []
        self._contents.append(deck.pop())
        self._contents.append(deck.pop())

    def __str__(self):
        retArray = ""
        for cards in self._contents:
            retArray += str(cards) + ", "
        return retArray

    def __gt__(self, hand2):
        if(self.get_value() > hand2.get_value()):
            return True
        else:
            return False

    def __lt__(self, hand2):
        if(self.get_value() < hand2.get_value()):
            return True
        else:
            return False

    def __ge__(self, hand2):
        if(self.get_value() >= hand2.get_value()):
            return True
        else:
            return False

    def __le__(self, hand2):
        if(self.get_value() <= hand2.get_value()):
            return True
        else:
            return False

    def __eq__(self, hand2):
        if(self.get_value() == hand2.get_value()):
            return True
        else:
            return False

    def __ne__(self, hand2):
        if(self.get_value() != hand2.get_value()):
            return True
        else:
            return False

    def hit(self, deck: Deck):
        self._contents.append(deck.pop())

    def get_value(self):
        total = 0
        numAces = 0
        for cards in self._contents:
            if cards.get_value() == 11:
                total += 11
                numAces += 1
            else:
                total += cards.get_value()
        if total > 21:
            return self.handle_aces(total, numAces)
        else:
            return total

    def handle_aces(selfself, total: int, numAces: int):
        while total > 21 and numAces > 0:
            total -= 10
            numAces -= 1
        return total

    def get_first_card(self):
        return self._contents[0]