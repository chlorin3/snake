from turtle import Turtle
FONT = ('Courier', 20, 'bold')
POSITION = (0, 270)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align="center", font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.refresh()


    def increase(self):
        self.score += 1
        self.refresh()
