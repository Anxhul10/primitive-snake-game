from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.position_change()
        self.speed("fastest")
        self.position_change()

    def position_change(self):
        rand_x = random.randint(-250, 250)
        rand_y = random.randint(-250, 250)
        self.goto(rand_x, rand_y)
