############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import os
from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def start_deal():
 user_cards= random.choices(cards,k=2)
 pc_cards= random.choices(cards,k=2)
 return {"user_cards":user_cards,"pc_cards":pc_cards}

def check_pc_status(pc):
  pc_score=0
  for card in pc:
    pc_score+=card
 
  if pc_score<17:
    new_pc_card=random.choice(cards)
    pc.append(new_pc_card)
    print(f"Computer gets new card, Computer new cards:{pc}, new card is {new_pc_card}, current score is {pc_score + new_pc_card}")
    check_pc_status(pc)
  else:
    if pc_score>21:
      print(f"You win, Computer cards was: {pc} with score: {pc_score}")
    elif pc_score>user_score:
      print(f"You lose, Computer cards was: {pc} with score: {pc_score}")
    elif pc_score<user_score:
      print(f"You win, Computer cards was: {pc} with score: {pc_score}")
    else:
      print("Draw")

def check_user_status(user,pc):
  user_score=0
  for card in user:
    user_score+=card
  
  if user_score>21:
    print(f'Bust, score:{user_score}')
  elif user_score<21:
    hit=input("Type 'y' to get another card, type 'n' to pass: ")
    if hit=='y':
      new_card=random.choice(cards)
      user.append(new_card)
      print(f"Your cards:{user}, new card is {new_card}, current score is {user_score + new_card}")
      check_user_status(user,pc)
    elif hit == 'n':
      check_pc_status(pc)
  else:
    print('Blackjack')

continue_play=True
while continue_play:
  want_play=input("Do you want to play Blackjack? Type 'y' or 'n': ")

  if want_play=='y':
    os.system('clear')
    print(logo)
    start_cards=start_deal()
    user_cards=start_cards['user_cards']
    pc_cards=start_cards['pc_cards']
    user_score=start_cards['user_cards'][0]+start_cards['user_cards'][1]
    print(f"Your cards:{user_cards}, current score:{user_score}")
    print(f"Computer's first cards:{pc_cards[0]}")
    check_user_status(user_cards,pc_cards)
  elif want_play=='n':
    continue_play=False