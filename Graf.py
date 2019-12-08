import turtle
blad = turtle.Screen()
graf = turtle.Pen()
graf.speed(0)
graf.goto(0,300)
graf.goto(0,-300)
graf.goto(0,0)
graf.goto(300,0)
graf.goto(-300,0)
first = True
for x in range(-300,301):
    if first:
        graf.penup()
    y = 1.5**x
    graf.goto(x,y)
    if first:
        graf.pendown()
        first = False
while True:
    pass
