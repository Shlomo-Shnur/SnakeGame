from turtle import Screen
from snake import Snake, SNAKE_HEAD
from food import Food
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_WIDTH_BORDER = SCREEN_WIDTH // 2 - 5
SCREEN_HEIGHT_BORDER = SCREEN_HEIGHT // 2 - 5

game_screen = Screen()
game_screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
game_screen.bgcolor("black")
game_screen.title("Snake Py")
game_screen.tracer(0)

snake = Snake()
food = Food()
game_score = Scoreboard()

game_screen.listen()
game_screen.onkey(snake.up, "Up")
game_screen.onkey(snake.down, "Down")
game_screen.onkey(snake.left, "Left")
game_screen.onkey(snake.right, "Right")


def check_walls_floors_collision():
    if snake.snake_body[SNAKE_HEAD].xcor() > SCREEN_WIDTH_BORDER or \
            snake.snake_body[SNAKE_HEAD].xcor() < -SCREEN_WIDTH_BORDER or \
            snake.snake_body[SNAKE_HEAD].ycor() > SCREEN_HEIGHT_BORDER or \
            snake.snake_body[SNAKE_HEAD].ycor() < -SCREEN_HEIGHT_BORDER:
        return True
    return False


game_is_on = True
while game_is_on:
    game_screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snake_body[SNAKE_HEAD].distance(food) < 15:
        game_score.increase_score()
        snake.grow()
        food.drop_food()
    if check_walls_floors_collision():
        game_is_on = False
        game_score.game_over()
    for segment in snake.snake_body[1:]:
        if snake.snake_body[SNAKE_HEAD].distance(segment) < 10:
            game_is_on = False
            game_score.game_over()

game_screen.exitonclick()
