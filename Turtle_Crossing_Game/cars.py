from turtle import Turtle
import random


class Cars:

    def __init__(self):
        self.spawn_list = []
        self.car_color_list = ["blue", "red", "orange", "cyan", "grey"]
        self.car_list = []
        self.car_speed = 20

    def generate_car(self):
        # Creates car objects, adds them to car list, and sets their heading based on spawn.
        car = Turtle("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.color(random.choice(self.car_color_list))
        placement = random.choice(self.spawn_list)
        car.goto(placement)
        if car.xcor() < -250:
            car.setheading(0)
        elif car.xcor() > 250:
            car.setheading(180)
        self.car_list.append(car)

    def randomize(self):
        # Randomizes the y cor for spawning based on lanes, some lanes designated for east heading, others for west.
        rand_y_left = random.randrange(-220, 260, 40)
        rand_y_right = random.randrange(-240, 240, 40)
        left_spawn = (-280, rand_y_left)
        right_spawn = (280, rand_y_right)
        self.spawn_list = [left_spawn, right_spawn]

    def move_car(self):
        # Move the car objects forward
        for car_object in self.car_list:
            car_object.forward(self.car_speed)

    def delete_car(self):
        """Delete car objects. This entails removal from car list and clearing of turtle object when end of screen
        reached"""
        for car in self.car_list:
            if car.heading() == 180 and car.xcor() < -300 or car.heading() == 0 and car.xcor() > 300:
                car.clear()
                car_order = self.car_list.index(car)
                self.car_list.pop(car_order)
