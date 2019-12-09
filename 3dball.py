maxvalue = 100
coordinates = [12,-34,15]
speeds = [12,9,13]
import turtle
import time
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
sscreen = turtle.Screen()
ball = turtle.Turtle()
wall = turtle.Turtle()
ball.ht()
ball.speed(0)
wall.ht()
wall.speed(0)
wall.penup()
wall.goto(maxvalue+10,maxvalue+10)
wall.pendown()
for i in range(0,4):
    wall.right(90)
    wall.forward((2*maxvalue)+20)
wall.goto((maxvalue*4)+20,maxvalue*4+20)
for i in range(0,4):
    wall.right(90)
    wall.forward((8*maxvalue)+40)
    wall.right(135)
    wall.fd((((3*maxvalue+10)**2)+((maxvalue*3+10)**2))**(1/2))
    wall.bk((((3*maxvalue+10)**2)+((maxvalue*3+10)**2))**(1/2))
    wall.left(135)
while True:
    ball.clear()
    ball.penup()
    ballsize = (coordinates[2] + maxvalue)+ 10
    ball.setposition(coordinates[0], coordinates[1]-(ballsize/2))
    ball.pendown()
    ball.circle(ballsize)
    move(0)
    move(1)
    move(2)
    time.sleep(0.02)