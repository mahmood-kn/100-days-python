import random

# exercise 1

# coin=random.randint(0,1)
# print("Flipping a coin ... ")

# if coin==0:
#   print("It's tails")
# else:
#   print("It's heads")

# exercise 2

# name_string=input("Give me everybody's names, separated by a comma.\n")
# names_list = name_string.split(", ")
# # random_idx=random.randint(0,len(names_list)-1)

# print(random.choice(names_list))

# exercise 3

# row1=["⬜","⬜","⬜"]
# row2=["⬜","⬜","⬜"]
# row3=["⬜","⬜","⬜"]
# map=[row1,row2,row3]

# print(f"{row1}\n{row2}\n{row3}")

# position=input("Where do you want to put the treasure? ")

# c=int(position[0])
# r=int(position[1])
# print(c,r)
# map[r-1][c-1]="X"
# # print(f"{map[0]}\n{map[1]}\n{map[2]}")
# print(f"{row1}\n{row2}\n{row3}")

# day exercise

# Rock
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

if user_choice>2 or user_choice<0:
  print("Input not valid")
  exit()

game_array=[rock,paper,scissors]

print(game_array[user_choice])

computer_choice=random.randint(0,2)
print(f'Computer Choice:\n{game_array[computer_choice]}')

if user_choice== computer_choice:
  print("It's draw")
else:
  if (user_choice==0 and computer_choice==1) or (user_choice==1 and computer_choice==2)or(user_choice==2 and computer_choice==0):
    print("You lose.")
  else:
    print("You Win.")