from snake import Snake
from food import Food
from score_board import Score
from turtle import Screen
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect Collision with Wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        game_on = False
        score.game_over()

    # Detect Collision with Tail
    # If head collides with any part the game is over.
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            game_on = False
            score.game_over()



screen.exitonclick()