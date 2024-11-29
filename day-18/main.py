from turtle import Turtle,Screen
import random
screen=Screen()
screen.colormode(255)
tt= Turtle()
tt.shape('turtle')
tt.color('blue')

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)
# exercise 1
# for _ in range(4):
#     tt.forward(100)
#     tt.right(90)

# exercise 2
# for _ in range(15):
#     tt.forward(10)
#     tt.penup()
#     tt.forward(10)
#     tt.pendown()

# exercise 3
# for i in range(3,11):
#     tt.color(random.choice(colors))
#     for j in range(i):
#         tt.forward(100)
#         tt.right(360/i)

# exercise 4
# tt.pensize(10)
# tt.shapesize(1.5)
# tt.speed(5)
# directions=[0,90,180,270]
# print(random_color())
# for _ in range(100):
#     tt.color(random_color())
#     tt.setheading(random.choice(directions))
#     tt.forward(30)

# exercise 5
tt.speed(0)
for i in range(72):
    tt.color(random_color())
    tt.circle(100)
    tt.left(5)
    

screen.exitonclick()
