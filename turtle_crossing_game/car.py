from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_DISTANCE = 10

class Car:
    def __init__(self):
        self.all_cars = []
        self.x = random.randint(-230, 300)
        self.speed = MOVE_DISTANCE
    def car_manager(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            tim = Turtle("square")
            tim.penup()
            tim.shape("square")
            tim.shapesize(stretch_wid=1,stretch_len=3)
            tim.speed(self.speed)
            y = random.randint(-230, 300)
            tim.goto(320, y)
            tim.color(random.choice(COLORS))
            self.all_cars.append(tim)

    def car_move(self):
        for cars in self.all_cars:
            cars.backward(self.speed)
    def level_up(self):
            self.speed += MOVE_DISTANCE



