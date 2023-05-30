import time
from turtle import Turtle

class Timer(Turtle):

    def __init__(self):
        super().__init__()
        self.start = time.time()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-290, 260)

    def write_time(self):
        self.write(arg=f"Time: {int(int(time.time()) - self.start)}", font=("Courier", 12, "normal"))

    def reset_time(self):
        self.start = int(int(time.time()))