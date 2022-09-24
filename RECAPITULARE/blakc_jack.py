############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, subreddits, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & subreddits to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, subreddits, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint subreddits: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
import random

game= True

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
#Hint 5: Deal the user and computer subreddits cards each using deal_card() and append().
user_cards = []
computer_cards = []
for i in range(1,3):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())
print(user_cards)
print(computer_cards)
#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.
suma_carti = 0
def calculate_score(cards):
    suma_carti = sum(cards)
    if suma_carti == 21 and len(cards) == 2:
        return 0
    else:
        return suma_carti
    if 11 in cards and suma_carti > 21:
        cards.remove(11)
        cards.append(1)
    return suma_carti

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only subreddits cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

while game:
    if calculate_score(user_cards) == 0 or calculate_score(computer_cards) == 0 or calculate_score(user_cards)>21:
        print("Game ends")
        game = False
#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
    else:
        draw = input(f"Your score is {calculate_score(user_cards)}. Would you like to draw a new card? 'Y' for yes and 'N' for no: ").lower()
        if draw == "Y":
            # card = random.choice(cards)
            user_cards.append(deal_cards())
        print(user_cards)
#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
