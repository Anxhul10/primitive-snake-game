import time
from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)

food = Food()
snake = Snake()
scoreBoard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


def self_bite():
    for part in snake.my_turtle[1:]:
        if snake.head.distance(part) < 15:
            return 1
    return 0


is_game_on = True
while is_game_on:
    screen.update()# refresh the screen
    time.sleep(0.1) # delay by 0.4s
    snake.move()

    if snake.my_turtle[0].distance(food) < 15:
        food.position_change()
        scoreBoard.score_update()
        snake.update_size_snake()
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        #is_game_on = False # position reset as well score
        snake.reset()
        scoreBoard.game_over()
    if self_bite():

        snake.reset()
        scoreBoard.game_over()
        #is_game_on = False # position reset as well score




screen.exitonclick()