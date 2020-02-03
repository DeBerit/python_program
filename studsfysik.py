import turtle
screen = turtle.Screen()
class Ball:
    def __init__(self, startpos, speed, color):
        self.turtle = turtle.Turtle()
        self.turtle.color(color)
        self.turtle.penup()
        self.pos = startpos
        self.speed = speed
        self.turtle.setpos(self.pos[0],self.pos[1])
        self.turtle.pendown()
    def switcharoo(self, reversex, reversey):
        switchvar = self.speed[0]
        self.speed[0] = self.speed[1]
        self.speed[1] = switchvar
        if reversex:
            self.speed[0] *= -1
        if reversey:
            self.speed[1] *= -1
    def move(self):
        for i in range(2):
            self.pos[i] += self.speed[i]
    def print(self):
        self.turtle.setpos(self.pos[0],self.pos[1])
    def combo(self):
        self.move()
        self.print()
boll = Ball([10, 50], [50, -30], "blue")
ball = Ball([10, 10], [50, 10], "red")
boll.combo()
ball.combo()
reversex = (boll.speed[1] > 0 and ball.speed[1] < 0) or (boll.speed[1] < 0 and ball.speed[1] > 0)
reversey = (boll.speed[0] > 0 and ball.speed[0] < 0) or (boll.speed[0] < 0 and ball.speed[0] > 0)
boll.switcharoo(reversex,reversey)
ball.switcharoo(reversex,reversey)
boll.combo()
ball.combo()
input()