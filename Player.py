class Player:
    def __init__(self):
        self._chips = 50

    def get_chips(self):
        return self._chips

    def lose_chips(self, chips: int):
        self._chips -= chips

    def gain_chips(self, chips: int):
        self._chips += chips

    def set_chips(self, chips: int):
        self._chips = chips