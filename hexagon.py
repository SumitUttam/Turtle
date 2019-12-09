import turtle
from random import randint,choice

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
hexagon = turtle.Turtle() 
hexagon.speed(1)
hexagon.right(randint(0,360))
x = randint(30,100)
hexagon.width(x/10-3)

for i in range(6):
    hexagon.color(choice(colors))
    hexagon.forward(x) 
    hexagon.right(60) 

hexagon.right(30)
for i in range(3):
    hexagon.color(choice(colors))
    hexagon.forward(x*(3**0.5)) 
    hexagon.right(120)

hexagon.left(30)
hexagon.color(choice(colors))
hexagon.forward(x)
hexagon.right(90) 

for i in range(3):
    hexagon.color(choice(colors))
    hexagon.forward(x*(3**0.5)) 
    hexagon.right(120)
      
turtle.done() 
