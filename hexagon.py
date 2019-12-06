import turtle
from random import randint
  
hexagon = turtle.Turtle() 
hexagon.speed(1)
hexagon.right(randint(0,360))
x = randint(30,100)

for i in range(6): 
    hexagon.forward(x) 
    hexagon.right(60) 

hexagon.right(30)
for i in range(3):
    hexagon.forward(x*(3**0.5)) 
    hexagon.right(120)

hexagon.left(30)
hexagon.forward(x)
hexagon.right(90) 

for i in range(3):
    hexagon.forward(x*(3**0.5)) 
    hexagon.right(120)
      
turtle.done() 