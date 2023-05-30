import turtle
from turtle import Turtle, Screen
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        with open(".\high_score.txt", mode="r") as file:
            self.highscore = int(file.read())
        self.penup()
        self.color("white")
        self.goto(0,260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}   Highest:{self.highscore}", align=ALIGNMENT, font=FONT)


    def increment(self):
        self.score += 1
        self.update_score()

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score=0
        with open(".\high_score.txt", mode="w") as file:
            file.write(f"{self.highscore}")
        self.update_score()
