from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    """This class inherits from the turtle module, and it creates a new scoreboard
    class it contains 3functions:
    
    > Update_scoreboard
    > increase_score
    > reset
    """

    def __init__(self):
        """Creates a scoreboard on the top middle of the screen, 
        opens the data text file and reads the high score"""
        super().__init__()
        self.score = 0
        with open("data.txt", mode='r', encoding="utf-8") as data:
            self.highscore = int(data.read())
            self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 265)
        self.update_scoreboard()

    def update_scoreboard(self):
        """updates the score board adn writes it out"""
        self.clear()
        self.write(arg=f"Score: {self.score} High score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """clears the screen every time a score is updated and updates the score by 1"""
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        """if the current score is bigger than the previous high score, then it updates it to the new one.
        also opens the data txt file and updates it there"""
        if self.score > self.highscore:
            self.highscore = self.score
        with open("data.txt", mode='w', encoding="utf-8") as data:
            data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()
