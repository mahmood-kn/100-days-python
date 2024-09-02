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
n=int(input('Check this number: '))

def prime_checker(number):
  is_prime=True
  if number== 1:
    print('1 is neither prime nor composite number.')
  else:
    for i in range(2,math.floor(number/2)+1):
      if number%i==0:
        is_prime=False
        break
  if is_prime:
    print(f'{number} is Prime')
  else:
    print(f'{number} is not Prime')
    

prime_checker(number=n)