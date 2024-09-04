from art import logo
import os
# exercise 1
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }

# student_grades={}

# for key in student_scores:
#   if student_scores[key]>90:
#     student_grades[key]="Outstanding"
#   elif student_scores[key]>80 :
#     student_grades[key]="Exceeds Expectations"
#   elif student_scores[key]>70 :
#     student_grades[key]="Acceptable"
#   else:
#     student_grades[key]="Fail"

# print(student_grades)

# exercise 2
# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇

# def add_new_country(country,visits,cities):
#   travel_log.append({
#     "country":country,
#     "visits":visits,
#     "cities":cities
#   })



# #🚨 Do not change the code below
# print(travel_log)
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

# day exercise

print(logo)
print("Welcome to the secret auction program.")
continue_bid=True
bids=[]

def find_winner(bids_record):
  highest=0
  highest_dict={}
  for key in range(len(bids_record)):
    if bids_record[key]["bid"]> highest:
      highest=bids_record[key]["bid"]
      highest_dict=bids_record[key]

  print(f"The winner is {highest_dict["name"]} with a bid of ${highest_dict["bid"]}.")

while continue_bid:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  new_bid={"name":name,"bid":bid}
  bids.append(new_bid)
  other_biders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if other_biders =='no':
    find_winner(bids)
    continue_bid=False
  elif other_biders=='yes':
    os.system('clear')
    