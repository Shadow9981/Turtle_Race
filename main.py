from turtle import Turtle, Screen
import random

screen = Screen()

race_on = False
screen.setup(500, 400)
user_bet = screen.textinput(title="Make a bet!", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for i in range(6):
    timmy = Turtle(shape="turtle")
    timmy.penup()
    timmy.color(colors[i])
    timmy.goto(x=-230, y=(-100 + (i * 35)))
    all_turtles.append(timmy)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            if turtle.pencolor() == user_bet:
                print(f"You've won! The {turtle.pencolor()} turtle is the winner!")
            else:
                print(f"You've lost! The {turtle.pencolor()} turtle is the winner!")

        turtle.forward(random.randint(0, 10))

screen.exitonclick()
