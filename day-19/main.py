from turtle import Turtle,Screen
import random
screen=Screen()
# exercise 1
# tim= Turtle()
# def move_forward():
#     tim.forward(10)

# def move_backward():
#     tim.backward(10)

# def move_clockwise():
#     tim.right(10)

# def move_counter_clockwise():
#     tim.left(10)
    
# def clear():
#     tim.penup()
#     tim.goto(0,0)
#     tim.clear()
#     tim.pendown()

# screen.listen()
# screen.onkey(key="w",fun=move_forward)
# screen.onkey(key="s",fun=move_backward)
# screen.onkey(key="d",fun=move_clockwise)
# screen.onkey(key="a",fun=move_counter_clockwise)
# screen.onkey(key="a",fun=move_counter_clockwise)
# screen.onkey(key="c",fun=clear)

# exercise 2
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
is_race_on=False
colors=["red","orange","yellow","green","blue","purple"]
all_turtles=[]

for i in range(len(colors)):
    new_turtle= Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230,y=-125+i*50)
    all_turtles.append(new_turtle)
    
if user_bet:
    is_race_on=True
while is_race_on:
    for turtle in (all_turtles):
        if round(turtle.xcor())>230:
            winning_color=turtle.pencolor()
            is_race_on=False
            if winning_color==user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")                
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")                
                
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)
    

screen.exitonclick()