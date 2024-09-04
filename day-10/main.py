from art import logo
# day exercise (calculator)

# Add
def add(n1,n2):
  return n1+n2
# Subtract
def subtract(n1,n2):
  return n1-n2
# multiply
def multiply(n1,n2):
  return n1*n2
# Divide
def divide(n1,n2):
  return n1/n2

operations={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}
print(logo)
def calculator():
  num1=float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  stop_operation=False
  while not stop_operation:
    operation_symbol=input("Pick an operation: ")
    num2=float(input("What's the next number?: "))
    answer=operations[operation_symbol](num1,num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")
    should_stop=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation or 'e' to exit.: ")
    if should_stop=='n':
      stop_operation=True
      calculator()
    elif should_stop=='y':
      num1=answer
    elif should_stop=='e':
      stop_operation=True
      
calculator()