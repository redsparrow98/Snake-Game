from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#####################  SCREEN  ###################
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# the tracker turns off the animations and we use update to show whats happened on screen
screen.tracer(0)
##################################################

# make the initial 3square snake object
snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

###################### GAME  #########################
game_is_on = True

while game_is_on:
    # use update at the start of each loop to see whats happened on screen
    screen.update()
    # slow down the time after each loop starts bu a little
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # detecting collision with tale
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()