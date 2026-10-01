# main.py
from deck import Deck
from hand import Hand

def main():
    deck = Deck()
    hand = Hand()
    hand.add_card(deck.deal_card())
    hand.add_card(deck.deal_card())
    print(hand)

if __name__ == '__main__':
    main()