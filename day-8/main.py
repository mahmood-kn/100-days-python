import math

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
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction_options=['encode','decode']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
if not direction in direction_options:
  print("Wrong input")
  exit()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text,shift_amount):
  encrypted=''
  for letter in plain_text:
    if letter in alphabet:
      index=alphabet.index(letter)
      if index+shift_amount>=len(alphabet):
        can_go=len(alphabet)-1 -index
        should_go_from_begin=shift_amount-can_go-1
        encrypted+=alphabet[should_go_from_begin]
        
      else:
        encrypted+=alphabet[index+shift_amount]
    else:
      encrypted+=letter
      
  print(f'The encoded text is: {encrypted}')

def decrypt(plain_text,shift_amount):
  decrypted=''
  for letter in plain_text:
    if  letter in alphabet:
      index=alphabet.index(letter)
      decrypted+=alphabet[index-shift_amount]
    else:
      decrypted+=letter
  print(f'The decoded text is: {decrypted}')

if direction=='encode':
  encrypt(plain_text=text,shift_amount=shift)
elif direction=='decode':
  decrypt(plain_text=text,shift_amount=shift)
