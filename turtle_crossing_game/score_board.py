from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.num = 1
        self.penup()
        self.hideturtle()
        self.goto(-250, 230)
        self.write(f"Level {self.num}", font=("Courier", 15, "normal"))

    def increase_level(self):
        self.num +=1
        self.clear()
        self.write(f"Level {self.num}", font=("Courier", 15, "normal"))

