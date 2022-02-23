import turtle



class Score(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.setposition(position)
        self.color("white")
        self.write(f"{self.score}", font=("david", 80))
        
        
    def score_count(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", font=("david", 80))

    def winner(self, who_won, end_score):
        self.setposition(-220,20)
        self.write(f"{who_won} player have won\n", font=("david", 40))
        self.setposition(-200,20)
        self.write(f"with the score of {end_score}", font=("david", 40))

    