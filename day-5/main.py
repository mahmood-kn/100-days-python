import random

# exercise 1
# student_heights=input("Input a list of student heights ").split()

# for n in range(0,len(student_heights)):
#   student_heights[n]=int(student_heights[n])

# # print(student_heights)

# sum =0
# for height in student_heights:
#   sum += height

# students=0
# for student in student_heights:
#   students+=1
# avg=round(sum/students)

# print(f"The average is {avg}")

# exercise 2
# student_scores=input("Input a list of student scores ").split()

# for n in range(0,len(student_scores)):
#   student_scores[n]=int(student_scores[n])


# highest =0
# for score in student_scores:
#   if score>highest:
#     highest=score

# print(f"The highest score in the class is: {highest}")

# exercise 3
# total=0
# for n in range(1,101,2):
#   total+=n
# print(total)

# exercise 4
# for n in range(0,101):
#   if n%3==0 and n%5==0:
#     print("FizzBuzz")
#   elif n%3==0:
#     print("Fizz")
#   elif n%5==0:
#     print("Buzz")
#   else:
#     print(n)

# day exercise

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~")

print('Welcome to the PyPassword Generator!')

nr_letters=int(input("How many letters would you like  in your password?\n"))
nr_symbols=int(input("How many symbols would you like  in your password?\n"))
nr_numbers=int(input("How many numbers would you like  in your password?\n"))

random_letters=''
random_symbols=''
random_numbers=''
for letter in range(1,nr_letters+1):
 random_letters+= random.choice(letters)

for symbol in range(1,nr_symbols+1):
 random_symbols+= random.choice(symbols)

for number in range(1,nr_numbers+1):
 random_numbers+= random.choice(numbers)

# easy
random_pass_easy=f"{random_letters}{random_symbols}{random_numbers}"
print(random_pass_easy)
# hard
# can do it with saving in an array and use random.shuffle(array)
random_pass_hard=''
for n in range(0,len(random_pass_easy)):
 chosen=random.choice(random_pass_easy)
 random_pass_hard+=chosen
 random_pass_easy=random_pass_easy.replace(chosen,'',1)

print(random_pass_hard)
