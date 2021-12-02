from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        # create list object to hold snake turtle objects
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        # set starting coordinates as variables to be changed later

        # create turtle objects to make initial snake
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        my_snake = Turtle()
        my_snake.speed(1)
        my_snake.shape("square")
        my_snake.color("white")
        my_snake.penup()
        my_snake.goto(position)
        self.snake_segments.append(my_snake)
        # my_snake = Turtle()
        # my_snake.speed(1)
        # my_snake.shape("square")
        # my_snake.penup()
        # # my_snake.setpos(self.snake_segments[-1].xcor() - 20, self.snake_segments[-1].ycor() - 20)
        # self.snake_segments.append(my_snake)
        # my_snake.color("white")

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            next_seg = self.snake_segments[seg_num - 1]
            self.snake_segments[seg_num].goto(next_seg.position())
        self.snake_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
