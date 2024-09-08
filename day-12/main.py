# day exercise - number guesser (My solution)

import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ") 

target=random.randint(1,100)
attempts=0
hit_the_target=False

def attempts_logger(remain):
  print(f"You have {remain} attempts remaining to guess the number.")

def set_attempts(user_choice):
  if user_choice=='easy':
    attempts_logger(10)
    return 10
  elif user_choice=='hard':
    attempts_logger(5)
    return 5

def decrease_attempts(prev_attempt):
  """Decrease the number of attempts"""
  attempts_left=prev_attempt-1
  attempts_logger(attempts_left)
  return attempts_left
  
attempts=set_attempts(difficulty)

while not hit_the_target and attempts!=0:
  guess=int(input("Make a guess: "))
  if guess>target:
    attempts=decrease_attempts(attempts)
    print("Too high")
  elif guess<target:
    attempts=decrease_attempts(attempts)
    print("Too low")
  else:
    print("You win!")
    hit_the_target=True

if not hit_the_target:
  print(f"You lose, the number was {target}")
    
