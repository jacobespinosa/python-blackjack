# deck.py
from card import Card
import random

class Deck:
    def __init__(self) -> None:
        self.cards = []
        suits = ['♠', '♥', '♦', '♣']
        ranks = ['2', '3', '4', '5', '6', '7', 
                 '8', '9', '10', 'J', 'Q', 'K', 'A']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

    def deal_card(self) -> Card:
        return self.cards.pop()

    def shuffle(self) -> None:
        random.shuffle(self.cards)