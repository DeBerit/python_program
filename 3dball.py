maxvalue = 300
coordinates = [-300,-300,-300]
speeds = [30,20,10]
import turtle
import time
sscreen = turtle.Screen()
ball = turtle.Turtle()
wall = turtle.Turtle()
ball.ht()
ball.speed(0)
wall.ht()
wall.speed(0)
wall.penup()
wall.goto(maxvalue,maxvalue)
wall.pendown()
for i in range(0,4):
    wall.right(90)
    wall.forward(2*maxvalue)
def move(dimension):
    global coordinates
    global speeds
    coordinates[dimension] = coordinates[dimension] + speeds[dimension]
    if coordinates[dimension] < maxvalue*-1:
        coordinates[dimension] = -1*maxvalue + ((-1*maxvalue)-coordinates[dimension])
        speeds[dimension] = speeds[dimension] * -1
    if coordinates[dimension] > maxvalue:
        coordinates[dimension] = maxvalue - (coordinates[dimension]-maxvalue)
        speeds[dimension] = speeds[dimension] * -1
while True:
    ball.clear()
    ball.penup()
    ball.setposition(coordinates[0], coordinates[1])
    ball.pendown()
    ballsize = (coordinates[2]+ maxvalue)*0.1 + 10
    ball.circle(ballsize)
    move(0)
    move(1)
    move(2)
    time.sleep(0.02)