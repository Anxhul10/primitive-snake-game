from turtle import Turtle

XCOR_LIST = [0, -20, -40]


class Snake:

    def __init__(self):
        self.my_turtle = []
        self.create_snake()
        self.head = self.my_turtle[0]
        self.move_speed = 20
        self.high_score = 0

    def create_snake(self):
        for i in range(0, 3):
            turtle = Turtle(shape="square")
            self.my_turtle.append(turtle)
            turtle.color("white")
            turtle.penup()
            turtle.goto(x=XCOR_LIST[i], y=0)
    def reset(self):

        for segments in self.my_turtle:
            segments.goto(1000, 1000)
        self.my_turtle.clear()
        self.create_snake()
        self.head = self.my_turtle[0]

    def update_size_snake(self):

        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(self.my_turtle[len(self.my_turtle)-1].xcor(), self.my_turtle[len(self.my_turtle)-1].ycor())
        self.my_turtle.append(new_turtle)

    def move(self):
        for position in range(len(self.my_turtle) - 1, 0, -1):
            new_x = self.my_turtle[position - 1].xcor()
            new_y = self.my_turtle[position - 1].ycor()
            self.my_turtle[position].goto(new_x, new_y)
        self.my_turtle[0].forward(20)

    def up(self):  # y + 1
        if self.my_turtle[0].heading() == 0:
            self.my_turtle[0].left(90)
        elif self.my_turtle[0].heading() == 180:
            self.my_turtle[0].right(90)

    def down(self):
        if self.my_turtle[0].heading() == 0:
            self.my_turtle[0].right(90)
        elif self.my_turtle[0].heading() == 180:
            self.my_turtle[0].left(90)

    def right(self):
        if self.my_turtle[0].heading() == 90:
            self.my_turtle[0].right(90)
        elif self.my_turtle[0].heading() == 270:
            self.my_turtle[0].left(90)

    def left(self):
        if self.my_turtle[0].heading() == 90:
            self.my_turtle[0].left(90)
        elif self.my_turtle[0].heading() == 270:
            self.my_turtle[0].right(90)
