import turtle

flag = turtle.Turtle()

flag.speed(4)
flag.pensize(5)
flag.color('#054187')
def draw(x,y):
    flag.penup()
    flag.goto(x,y)
    flag.pendown()
    


for i in range(24):
    flag.forward(60)
    flag.backward(60)
    flag.left(15)

draw(0, -60) 
flag.circle(60, 360)


    
flag.color('green')
draw(0,-70)
flag.begin_fill()
flag.forward(350)
flag.backward(700)
flag.right(90)
flag.forward(200)
flag.left(90)
flag.forward(700)
flag.left(90)
flag.forward(200)
flag.left(90)
flag.end_fill()

flag.color('orange')
draw(-350,70)
flag.begin_fill()
flag.right(180)
flag.forward(700)
flag.left(90)
flag.forward(200)
flag.left(90)
flag.forward(700)
flag.left(90)
flag.forward(200)
flag.end_fill()
    
turtle.done()