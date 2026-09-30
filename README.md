# Python Blackjack

A command-line Blackjack game built to practice object-oriented programming in Python.

## OOP Design

### Card

**Attributes**
 - rank
 - suit

**Methods**
 - get_value

### Deck

**Attributes**
 - cards 

**Methods**
 - shuffle
 - deal_card

### Player

**Attributes**
 - bankroll
 - hand/hands
 - bet

**Methods**
 - hit
 - stand
 - double_down
 - split
 - place_bet
 - set_bankroll

### Hand

**Attributes**
 - cards

**Methods**
 - get_value
 - add_card
 - is_bust

### Dealer
Inherits from `Player`.

**Inherited Attributes**
- hand

**Methods**
- play_turn
- reveal_hidden_card

### BlackjackGame

**Attributes**
 - deck
 - player
 - dealer

**Methods**
 - start_game
 - end_game
 - new_round
 - deal_cards
 - player_turn
 - dealer_turn
 - check_winner




