from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 260)
        with open("high_score_data.txt") as data:
            self.highscore = int(data.read())
        self.show_score()

    def increase_score(self):
        self.count += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.count} High Score: {self.highscore}", align = ALIGNMENT, font = FONT)

    def reset(self):
        if self.count > self.highscore:
            self.highscore = self.count
            with open("high_score_data.txt", mode = "w") as data:
                data.write(f"{self.highscore}")
        self.count = 0
        self.show_score()