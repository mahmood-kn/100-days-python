import math
from art import logo 
# exercise 1

# test_h= int(input("Height of wall: "))
# test_w= int(input("Width of wall: "))
# coverage=5

# def paint_calc(height,width,cover):
#   return math.ceil((height*width)/cover)

# cans=paint_calc(height=test_h,width=test_w,cover=coverage)

# print(f"You'll need {cans} cans of paint.")

# exercise 2 (prime number checker)
# n=int(input('Check this number: '))

# def prime_checker(number):
#   is_prime=True
#   if number== 1:
#     print('1 is neither prime nor composite number.')
#   else:
#     for i in range(2,math.floor(number/2)+1):
#       if number%i==0:
#         is_prime=False
#         break
#   if is_prime:
#     print(f'{number} is Prime')
#   else:
#     print(f'{number} is not Prime')
    

# prime_checker(number=n)

# day project
#            0    1    2    3    4
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction_options=['encode','decode']
print(logo)


def ceasar(text,shift,direction):
  end_text=''
  if direction=='decode':
    shift *=-1
  for letter in text:
    if  letter in alphabet:
      position=alphabet.index(letter)
      new_position=position+shift
      end_text+=alphabet[new_position]
    else:
      end_text+=letter
  print(f'The {direction}d text is: {end_text}')

should_continue=True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  if not direction in direction_options:
    print("Wrong input")
    exit()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift=shift%26
  ceasar(text,shift,direction)
  run_again=input("Type 'yes' if you want to go again, otherwise type 'no'.\n").lower()
  if run_again=='no':
    should_continue=False
    print("GoodBye")