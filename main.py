from turtle import Screen, Turtle
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bets", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


def display_text(text, result):
    display_turtle = Turtle()
    display_turtle.hideturtle()
    display_turtle.penup()
    display_turtle.goto(0, 160)
    display_turtle.pendown()
    if result:
        display_turtle.write(f"Congrats. You've won! The {text} turtle is the winner.", font=("Arial", 12, "normal"),
                             align="center")
    else:
        display_turtle.write(f"I'm sorry. You've lost! The {text} turtle is the winner.", font=("Arial", 12, "normal"),
                             align="center")


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                display_text(text=winning_color, result=True)
            else:
                display_text(text=winning_color, result=False)
            break

screen.exitonclick()
