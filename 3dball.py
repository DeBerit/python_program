maxvalue = 100  # The boundries of the box in which the ball is bouncing
coordinates = [-100,-100,-100]  #starting position for ball
speeds = [6,12,13]  #how much the ball travels in each direction
import turtle
import time
def move(dimension):
    global coordinates
    global speeds
    coordinates[dimension] = coordinates[dimension] + speeds[dimension] # The ball is moved.
    if coordinates[dimension] < maxvalue*-1:    # The ball "bounces" if it is outside the boundry.
        coordinates[dimension] = -1*maxvalue + ((-1*maxvalue)-coordinates[dimension])
        speeds[dimension] = speeds[dimension] * -1
    if coordinates[dimension] > maxvalue:   # The ball "bounces" if it is outside the boundry.
        coordinates[dimension] = maxvalue - (coordinates[dimension]-maxvalue)
        speeds[dimension] = speeds[dimension] * -1
screen = turtle.Screen()
screen.screensize(((6*maxvalue)+20),((6*maxvalue)+20))
ball = turtle.Turtle()
wall = turtle.Turtle()
ball.ht()
ball.speed(0)
wall.ht()
wall.speed(0)
wall.penup()
wall.goto(maxvalue+10,maxvalue+10)
wall.pendown()
for i in range(0,4):    #the small square is drawn.
    wall.right(90)
    wall.forward((2*maxvalue)+20)
wall.goto((maxvalue*3)+10,maxvalue*3+10)    # The larger outer square is drawn.
for i in range(0,4):
    wall.right(90)
    wall.forward((6*maxvalue)+20)
    wall.right(135)
    wall.fd((((2*maxvalue)**2)+((maxvalue*2)**2))**(1/2))   # lines going to the inner square are drawn. Their length is calculated using the pythagorean theorem.
    wall.bk((((2*maxvalue)**2)+((maxvalue*2)**2))**(1/2))
    wall.left(135)
while True:
    ball.clear()
    ball.penup()
    ballsize = (coordinates[2] + maxvalue)+ 10  # the ball is bigger the closer it is to the "camera".
    ball.setposition(coordinates[0], coordinates[1]-(ballsize)) # the turtle is moved so that the center of the circle is at the balls position
    ball.pendown()
    ball.circle(ballsize)
    move(0)
    move(1)
    move(2)
    time.sleep(1/61)    #60fps
