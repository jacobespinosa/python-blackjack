# participant.py
from abc import ABC, abstractmethod
from hand import Hand
from card import Card
from deck import Deck

FIRST_HAND = 0

class Participant(ABC):
    def __init__(self) -> None:
        self.hands = [Hand()]

    @abstractmethod
    def play_turn(self, deck: Deck) -> None:
        pass

class Player(Participant):
    def __init__(self, bankroll: int) -> None:
        super().__init__()
        self.bankroll = bankroll

    def double_down(self, card: Card, hand_num: int = 0) -> bool:
            self.bankroll -= self.hands[hand_num].bet
            self.hands[hand_num].bet *=  2
            self.hands[hand_num].add_card(card)
            return self.hands[hand_num].is_bust()

    def split(self, hand_num: int = FIRST_HAND) -> None:
        new_hand = Hand(self.initial_bet)
        card = self.hands[hand_num].cards.pop()
        new_hand.add_card(card)
        self.hands.append(new_hand)

    def place_bet(self, bet: int) -> bool:
        if bet <= 0:
            raise ValueError("Bet must be greater than 0.")
        elif bet > self.bankroll:
            raise ValueError("Bet must be less than or equal to bankroll.")
        else:
            self.bankroll -= bet
            self.hands[FIRST_HAND].bet = bet

    def get_player_choice(self) -> int:
        while True:
            choice = input("\n1. hit\n2. stand\n3. double down\n4. split\n")
            trim_choice = choice.lower().strip()

            # Valid number
            if trim_choice.isdigit() and (int(trim_choice) > 0 and int(trim_choice) < 5):
                break
            elif trim_choice in ("hit", "stand", "double down", "split"):
                break
            else:
                if not trim_choice.isdigit():
                    print("Invalid input: Choose: 'hit', 'stand', 'double down', or 'split'\n")
                else:
                    print("Invalid input: Choose number between 1 and 4\n")

        # Convert string choice to integer
        if not trim_choice.isdigit():
            match trim_choice:
                case "hit": trim_choice = 1
                case "stand": trim_choice = 2
                case "double down": trim_choice = 3
                case "split": trim_choice = 4
        else:
            trim_choice = int(trim_choice)

        return trim_choice



    def play_turn(self, deck: Deck) -> None:
        print(self.hands)

        for hand_num, hand in enumerate(self.hands):
            is_bust = False
            is_stand = False
            is_double_down = False
            while not is_bust and not is_stand and not is_double_down:

                choice = self.get_player_choice()

                match choice:
                    case 1: 
                        hand.add_card(deck.deal_card())
                        is_bust = hand.is_bust()
                    case 2: is_stand = True
                    case 3: 
                        if len(hand.cards) != 2:
                            print("Can only split on first choice.")
                        elif hand.bet > self.bankroll:
                            print("Not enough in bankroll to double down.")
                        else:
                            is_bust = self.double_down(deck.deal_card(), hand_num)
                            is_double_down = True
                    case 4: 
                        if len(hand.cards) != 2:
                            print("Can only split on 2 cards")
                        elif hand.bet > self.bankroll:
                            print("Not enough in bankroll to split.")
                        elif self.hands[hand_num].cards[0].rank == self.hands[hand_num].cards[1].rank:
                            print("Can't split a hand unless both cards have same rank.")
                        else:
                            self.split(hand_num)