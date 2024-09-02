import math

# exercise 1

test_h= int(input("Height of wall: "))
test_w= int(input("Width of wall: "))
coverage=5

def paint_calc(height,width,cover):
  return math.ceil((height*width)/cover)

cans=paint_calc(height=test_h,width=test_w,cover=coverage)

print(f"You'll need {cans} cans of paint.")
