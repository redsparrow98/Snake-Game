from turtle import Turtle
import random

class Food(Turtle):
    """This class inherits from turtle module and it creates the food in the game"""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("purple")
        self.speed(0)
        self.refresh()

    def refresh(self):
        """This function refreshes the food square at a random point on the screen"""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
