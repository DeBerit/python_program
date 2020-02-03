import turtle
import math
scale = (1)
maxvalue = 100
x = maxvalue
invalid = False
class Graph:
    def __init__(self, color, function):
        self.turtle = turtle.Turtle()
        self.turtle.ht()
        self.turtle.speed(0)
        self.function = function
        self.turtle.color()
    def func(self):
        function = self.function()
        y = eval(function)
        return y
screen = turtle.Screen()
axis = turtle.Turtle()
axis.ht()
for i in range(4):
    axis.fd(maxvalue/scale)
    axis.bk(maxvalue/scale)
    axis.left(90)
num_graph = int(input("how many graphs?"))
graph = []
for i in range(num_graph):
    graph.append(Graph(input("color?"),input("y = ")))
    graph[i].turtle.speed(0)
    graph[i].turtle.ht()
    graph[i].turtle.pu()
    graph[i].turtle.goto((maxvalue/scale), graph[i].func())
while x <= maxvalue:
    for i in range(num_graph):
        try:
            y = graph[i].func()
            if not invalid:
                graph[i].turtle.pd()
            graph[i].turtle.goto(x,y)
            graph[i].turtle.pu()
            invalid = False
        except:
            invalid = True
        x += scale
input()