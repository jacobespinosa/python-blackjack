# hand.py
from card import Card

class Hand:
    def __init__(self, bet: int) -> None:
        self.cards = []
        self.bet = bet
        self.is_bust = False

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def get_value(self) -> int:
        value = 0
        aces = 0

        for card in self.cards:
            value += card.get_value()

            if card.rank == 'A':
                aces += 1

        while value > 21 and aces > 0:
            value -= 10
            aces -= 1

        return value

    def is_bust(self) -> bool:
        return self.get_value() > 21

    def can_split(self) -> bool:
        pass

    def can_double_down(self) -> bool:
        pass

    def __str__(self) -> str:
        handStr = ""
        for card in self.cards:
            handStr += f"{card} "
        return handStr