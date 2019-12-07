import turtle
colors = ['red', 'white', 'blue', 'green', 'orange', 'yellow'] 
turtle.setup(1280,720)
turtle.bgcolor('black')
turtle.speed(0)
for i in range(2000):
    turtle.color(colors[i%3])
    turtle.fd(i)
    turtle.rt(121)