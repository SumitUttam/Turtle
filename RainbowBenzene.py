import turtle 
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
RainbowBenzene = turtle.Pen() 
turtle.bgcolor('black') 
RainbowBenzene.shape('turtle')
RainbowBenzene.speed(0)
for x in range(360): 
    RainbowBenzene.pencolor(colors[x%6]) 
    RainbowBenzene.width(x/100 + 1) 
    RainbowBenzene.forward(x/2) 
    RainbowBenzene.left(59)

input() 