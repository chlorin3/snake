from turtle import Turtle
FONT = ('Courier', 20, 'bold')
POSITION = (0, 270)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        self.score = 0
        self.refresh()

    def refresh(self):
        self.write(f"Score: {self.score}", move=False, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.refresh()
