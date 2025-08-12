from turtle import Turtle, Screen
from car import Car
import time
from score_board import ScoreBoard

turtle= Turtle(shape="turtle")
screen = Screen()
screen.screensize(400,400)
screen.tracer(0)

def movement():
    turtle.penup()
    turtle.goto(0,-250)
    turtle.left(90)

def move_up():
    turtle.forward(10)
screen.onkey(move_up, "Up")
screen.listen()

movement()
car = Car()
score = ScoreBoard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.car_manager()
    car.car_move()
    if turtle.ycor() == 250:
        turtle.goto(0,-250)
        car.level_up()
        score.increase_level()



    for cars in car.all_cars:
        if cars.distance(turtle) < 15:
            tem = Turtle()
            tem.write("GAME OVER", align="center", font=("Courier", 25, "bold"))
            game_is_on = False



screen.mainloop()