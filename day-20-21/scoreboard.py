from turtle import Turtle
ALIGNMENT="center"
FONT=('courier', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.update_score()
    def update_score(self):
        self.goto(0,270)
        self.write(arg=f'score: {self.score}',move=True,align=ALIGNMENT,font=FONT)
        
        
    def get_point(self):
        self.clear()
        self.score+=1
        self.update_score()
        
        
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",move=True,align=ALIGNMENT,font=FONT)