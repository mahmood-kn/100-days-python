# a = 123
# b=str(a)
# print(type(b))

# print(70+float(120))

#  exercise 1

# num =input("Type a two digit number: ")
# print(int(num[0])+int(num[1]))

#  exercise 2 Bmi

# height = input("Enter your height in m: ")
# weight = input("Enter your weight in kg: ")

# bmi = float(weight)/(float(height)**2)
# print("Your bmi is: "+str(int(bmi)))

# rounding numbers
# print(round(2.6666,2))
# print(8//2)
# res= 4/2
# res /= 2
# res += 2
# res -= 2
# res *= 2

# f-string

# score =0 
# height =1.8 
# is_winning=True
# print(f"your score is {score}, your height is {height},you winning state is {is_winning}")

# exercise 3

# age =input("What is your current age? ")
# int_age=int(age)

# age_remain=90-int_age

# days=age_remain*365
# week=age_remain*52
# month=age_remain*12

# print(f"You have {days} days, {week} weeks and {month} months left.")

# day 2 exercise

print("Welcome to the tip calculator.")
total_bill=input("What was the total bill? ")
percentage=input("What percentage tip would you like to give? 10, 12, or 15? ")
people=input("How many people to split the bill? ")

total_bill_float=float(total_bill)
percentage_float=float(percentage)
people_int=int(people)

person_bill= (total_bill_float+((total_bill_float*percentage_float)/100))/people_int
final_bill="{:.2f}".format(person_bill)

print(f"Each person should pay: ${final_bill}")