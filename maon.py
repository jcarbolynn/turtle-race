from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500,height=400)

user_bet = screen.textinput(title="make your bets now", prompt="which turtle will win the race? (color)")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=-70 + (turtle_index*30))
    all_turtles.append(new_turtle)

# no way to change position based on for loop without creating another variable that increases with each color
# for color in colors:
#   name = str(color)
#   name = Turtle(shape = "turtle")
#   name.color(color)
#   name.penup()
#   name.goto(x=-240, y=-100)

if user_bet:
  race_on = True

# so race only starts after user made a bet
while race_on:
  for turtle in all_turtles:
    # race ends when turtle middle hits edge of screen, turtle object is 40x40 (250 - 40/2 = 230)
    if turtle.xcor() > 230:
      race_on = False
      winning_color = turtle.pencolor()
      if winning_color == user_bet:
        print(f"You won! The {winning_color} turtle won")
      else:
        print(f"You lost! The {winning_color} turtle won")
    
    distance = random.randint(0,10) #(inclusive)
    turtle.forward(distance)


#keeps screen open until you close it by clicking on the screen
screen.exitonclick()
