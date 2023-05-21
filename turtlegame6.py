# Turtle Graphics Game – Space Turtle Chomp

import turtle
import math
import random


# Set up screen
turtle.setup(650, 650)
wn = turtle.Screen()
wn.bgcolor('navy')

# Draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(2)
mypen.color('white')
mypen.speed(0)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

# Create player turtle
player = turtle.Turtle()
player.color('olive')
player.shape('turtle')
player.penup()
player.speed(0)

# Create food
food = turtle.Turtle()
food.color("yellow")
food.shape("circle")
food.penup()
food.speed(0)
#food.setposition(-100, 100) 
food.setposition(random.randint(-290, 290), random.randint(-290, 290))

# Set speed variable
speed = 1

# Define functions
def turn_left():
    player.left(30)

def turn_right():
    player.right(30)

def increase_speed():
    global speed
    speed += 1

def decrease_speed():
    global speed
    if speed > 1:
        speed -= 1

def isCollision(t1, t2):
       d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
       if d < 20:
           return True
       else:
           return False

# Set keyboard binding
turtle.listen()
turtle.onkey(turn_left, 'Left')
turtle.onkey(turn_right, 'Right')
turtle.onkey(increase_speed, 'Up')
turtle.onkey(decrease_speed, 'Down')

while True:
    player.forward(speed)

    # Boundary Player Checking x coordinate
    if player.xcor() > 290 or player.xcor() < -290:
        player.right(180)

    # Boundary Player Checking y coordinate
    if player.ycor() > 290 or player.ycor() < -290:
        player.right(180)

    # Boundary Food Checking x coordinate
    if food.xcor() > 290 or food.xcor() < -290:
        food.right(180)

    # Boundary Food Checking y coordinate
    if food.ycor() > 290 or food.ycor() < -290:
        food.right(180)

    # Move food around
    food.forward(3)

    # Collision checking
    if isCollision(player, food):
        food.setposition(random.randint(-290, 290), random.randint(-290, 290))
        food.right(random.randint(0, 360))
