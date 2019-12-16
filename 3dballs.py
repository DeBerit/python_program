maxvalue = 110  # The boundries of the box in which the ball is bouncing
speeds = [6,12,13]  #how much the ball travels in each direction
import turtle
import time
number_of_balls = 3
class Ball:
    def __init__(self,x,y,z,vx,vy,vz,size,color):
        self.turtle = turtle.Turtle()
        self.coordinates = [x,y,z] #startingposition for ball
        self.speeds = [vx,vy,vz]
        self.size = size
        self.max = maxvalue - size
        self.turtle.color(color)
        self.turtle.ht()
        self.turtle.speed(0)
    def move_in_one_dimension(self,dimension):
        self.coordinates[dimension] = self.coordinates[dimension] + self.speeds[dimension] # The ball is moved.
        if self.coordinates[dimension] < self.max*-1:    # The ball "bounces" if it is outside the boundry.
            self.coordinates[dimension] = -1*self.max + ((-1*self.max)-self.coordinates[dimension])
            self.speeds[dimension] = self.speeds[dimension] * -1
        if self.coordinates[dimension] > self.max:   # The ball "bounces" if it is outside the boundry.
            self.coordinates[dimension] = self.max - (self.coordinates[dimension]-self.max)
            self.speeds[dimension] = self.speeds[dimension] * -1
    def move(self):
        self.move_in_one_dimension(0)
        self.move_in_one_dimension(1)
        self.move_in_one_dimension(2)
    def drawball(self):
        self.turtle.clear()
        self.turtle.penup()
        ballsize = (self.coordinates[2] + self.max)+ self.size  # the ball is bigger the closer to the "camera" it is.
        self.turtle.setposition(self.coordinates[0], self.coordinates[1]-(ballsize)) # the turtle is moved so that the center of the circle is at the balls position
        self.turtle.pendown()
        self.turtle.circle(ballsize)
screen = turtle.Screen()
screen.screensize(((6*maxvalue)),((6*maxvalue)))
ball = turtle.Turtle()
wall = turtle.Turtle()
ball.ht()
ball.speed(0)
wall.ht()
wall.speed(0)
wall.penup()
wall.goto(maxvalue,maxvalue)
wall.pendown()
balls = [1,2,3]
balls[0] = Ball(10,-40,-130,12,15,-14,10,"blue")
balls[1] = Ball(0,0,0,12,34,12,5,"red")
balls[2] = Ball(34,-50,-130,32,15,-14,9,"Black")
for i in range(0,4):    #the small square is drawn.
    wall.right(90)
    wall.forward((2*maxvalue))
wall.goto((maxvalue*3),maxvalue*3)    # The larger outer square is drawn.
for i in range(0,4):
    wall.right(90)
    wall.forward((6*maxvalue))
    wall.right(135)
    wall.fd((((2*maxvalue)**2)+((maxvalue*2)**2))**(1/2))   # lines going to the inner square are drawn. Their length is calculated using the pythagorean theorem.
    wall.bk((((2*maxvalue)**2)+((maxvalue*2)**2))**(1/2))
    wall.left(135)
while True:
    for i in range(0,number_of_balls):
        balls[i].drawball()
    for i in range(0,number_of_balls):
        balls[i].move()
    time.sleep(1/61)    #60fps