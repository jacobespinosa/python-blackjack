# card.py

class Card:
    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit

    def get_value(self) -> int:
        if self.rank == 'A':
            return 11
        elif self.rank.isdigit():
            return int(self.rank)
        else:
            return 10
