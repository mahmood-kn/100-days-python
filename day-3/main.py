# exercise 1
# num =input("Enter a number: ")

# num_float=float(num)

# if num_float % 2==0:
#   print("The number is even")
# else:
#   print("The number is odd")

# exercise 2 
# height = input("Enter your height in m: ")
# weight = input("Enter your weight in kg: ")

# bmi = round(float(weight)/(float(height)**2))

# if bmi < 18.5:
#   print(f"Your bmi is {bmi} and you are underweight")
# elif bmi < 25:
#   print(f"Your bmi is {bmi} and you are normal")
# elif bmi<30:
#   print(f"Your bmi is {bmi} and you are overweight")
# elif bmi<35:
#   print(f"Your bmi is {bmi} and you are obese")
# else:
#   print(f"Your bmi is {bmi} and you are clinically obese")
  
# exercise 3
# num =input("Enter a year: ")

# num_float=float(num)

# if num_float % 4== 0:
#   if num_float % 100 == 0:
#     if num_float% 400==0:
#       print('leap year')  
#     else:
#       print('Not leap year')  
#   else:
#     print('Not leap year')  
# else:
#   print('Not leap year')  

# exercise 4
# print('Welcome to Python Pizza Deliveries!')
# size = input("What size pizza do you want? S, M, or L  ")
# add_pepperoni = input("Do you want pepperoni? Y or N  ")
# extra_cheese = input("Do you want extra cheese? Y or N  ")

# bill =0
# if size=="S":
#   bill +=15
#   if add_pepperoni=="Y":
#     bill+=2
# elif size=="M":
#   bill +=20
#   if add_pepperoni=="Y":
#     bill+=3
# elif size=="L":
#   bill +=25
#   if add_pepperoni=="Y":
#     bill+=3

# if extra_cheese=="Y":
#   bill+=1

# print(f'Your final bill is: ${bill}')

# exercise 5

# print("Welcome to the Love Calculator")
# name1= input("What is your name? \n")
# name2= input("What is their name? \n")

# lower_name1=name1.lower()
# lower_name2=name2.lower()

# true_text="true"
# love_text="love"
# true_count=0
# love_count=0

# true_count+=lower_name1.count(true_text[0])
# true_count+=lower_name1.count(true_text[1])
# true_count+=lower_name1.count(true_text[2])
# true_count+=lower_name1.count(true_text[3])
# true_count+=lower_name2.count(true_text[0])
# true_count+=lower_name2.count(true_text[1])
# true_count+=lower_name2.count(true_text[2])
# true_count+=lower_name2.count(true_text[3])

# love_count+=lower_name1.count(love_text[0])
# love_count+=lower_name1.count(love_text[1])
# love_count+=lower_name1.count(love_text[2])
# love_count+=lower_name1.count(love_text[3])
# love_count+=lower_name2.count(love_text[0])
# love_count+=lower_name2.count(love_text[1])
# love_count+=lower_name2.count(love_text[2])
# love_count+=lower_name2.count(love_text[3])

# percent = int(f'{true_count}{love_count}')

# if percent<10 or percent>90:
#   print(f'Your score is {percent}, you go together like coke and mentos.')
# elif percent>=40 and percent<=50:
#   print(f'Your score is {percent}, you are alright together.')
# else:
#   print(f'Your score is {percent}.')

# day 3 main project

print('''
  .     '     ,
    _________
 _ /_|_____|_\ _
   '. \   / .'
     '.\ /.'
       '.'
''')
print("")
direction=input('left or right: ')

if direction=='right':
  print("Game over")
elif direction=='left':
  s_w=input("swim or wait: ")
  if s_w=='swim':
    print("Game over")
  elif s_w=='wait':
    door=input("Which door? blue, yellow or red: ")
    if door == 'blue' or door=='red':
      print("Game over")
    elif door=='yellow':
      print("You Win!")

