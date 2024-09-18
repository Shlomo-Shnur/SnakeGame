from turtle import Turtle

TURTLE_SIZE = MOVE_DISTANCE = 20
SNAKE_HEAD = RIGHT = 0
LAST_SEGMENT = -1
UP = 90
DOWN = 270
LEFT = 180


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()

    def move(self):
        for segment_number in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[segment_number - 1].xcor()
            new_y = self.snake_body[segment_number - 1].ycor()
            self.snake_body[segment_number].goto(new_x, new_y)
        self.snake_body[SNAKE_HEAD].forward(MOVE_DISTANCE)

    def create_snake(self):
        for index in range(3):
            self.grow()

    def up(self):
        if self.snake_body[SNAKE_HEAD].heading() != DOWN:
            self.snake_body[SNAKE_HEAD].setheading(UP)

    def down(self):
        if self.snake_body[SNAKE_HEAD].heading() != UP:
            self.snake_body[SNAKE_HEAD].setheading(DOWN)

    def left(self):
        if self.snake_body[SNAKE_HEAD].heading() != RIGHT:
            self.snake_body[SNAKE_HEAD].setheading(LEFT)

    def right(self):
        if self.snake_body[SNAKE_HEAD].heading() != LEFT:
            self.snake_body[SNAKE_HEAD].setheading(RIGHT)

    def grow(self):
        if not self.snake_body:
            xcor = ycor = 0
        elif len(self.snake_body) < 3:
            xcor = self.snake_body[LAST_SEGMENT].xcor() - 20
            ycor = 0
        else:
            xcor, ycor = self.snake_body[LAST_SEGMENT].position()
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(x=xcor, y=ycor)
        self.snake_body.append(new_segment)
