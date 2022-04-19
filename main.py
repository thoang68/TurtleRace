from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet',
                            prompt='Which turtle will win the race? Enter a color('
                                   'blue/red/orange/yellow/green/purple): ')
colors = ['blue', 'red', 'orange', 'yellow', 'green', 'purple']

print(f"Your bet is {user_bet}.")
is_game_on = False
if user_bet in colors:
    is_game_on = True
else:
    print(f"{user_bet} is an invalid color choice. Quit game.")
    quit()

y_pos = -100
all_turtles = []
for c in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(c)
    new_turtle.goto(x=-240, y=y_pos)
    y_pos += 40
    all_turtles.append(new_turtle)

while is_game_on:
    for turtle in all_turtles:
        random_move = random.randint(1, 10)
        turtle.forward(random_move)
        if turtle.xcor() >= 250 - (40 / 2):
            is_game_on = False
            winning_turtle = turtle.pencolor()
            if user_bet == winning_turtle:
                print(f"You've won! The {winning_turtle} turtle is the winner")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner")
            break

screen.exitonclick()