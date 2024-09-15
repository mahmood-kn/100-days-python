from art import logo,vs
import random
from game_data import data
import os


def get_random_item():
  return random.choice(data)

def print_contest(first,score):
  os.system('clear')
  random_a=first
  random_b=get_random_item()
  while random_a == random_b:
    random_b=get_random_item()
    
  # print(f"A:{random_a['follower_count']}")
  # print(f"B:{random_b['follower_count']}")
  print(logo)
  if score>0:
    print(f"Your score is: {score}")
  compare_a=f"Compare A: {random_a["name"]}, a {random_a['description']}, from {random_a['country']}"
  compare_b=f"Compare B: {random_b["name"]}, a {random_b['description']}, from {random_b['country']}"

  print(compare_a)
  print(vs)
  print(compare_b)


  choice= input("Who has more follower_count? Type 'A' or 'B': ").lower()
  return analyse_result(choice,score,random_a,random_b)

def analyse_result(choice,prev_score,random_a,random_b):
  new_score=prev_score+1
  if choice=="a" and random_a['follower_count']>=random_b['follower_count']:
    return random_a,new_score
  elif choice=="b" and random_b['follower_count']>random_a['follower_count']:
    return random_b,new_score
  else:
    return None,score
    
score=0
random_a=get_random_item()
continue_playing=True

while continue_playing:
  random_a,score=print_contest(random_a,score)
  if random_a is None:
    continue_playing=False
    print(f"You lose, Your final score is: {score}")