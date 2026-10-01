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

### Hand

**Attributes**
 - cards

**Methods**
 - get_value
 - add_card
 - is_bust

### Participant

**Attributes**
 - hand/hands

**Methods**
 - play_turn

### Player
Inherits from `Participant`

**Additional Attributes**
 - bankroll
 - bet

**Additional/Override Methods**
 - double_down
 - split
 - place_bet
 - play_turn

### Dealer
Inherits from `Participant`.

**Additional Attributes**
- None

**Additional/Override Methods**
- play_turn

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
 - reveal_hidden_card




