import turtle
from datetime import datetime

turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.goto(0, 0)
turtle.tracer(0)  
turtle.bgcolor("BLUE")

while True:
    turtle.clear()
    
    now = datetime.now()
    HOUR = now.hour % 12
    MINUTE = now.minute
    SECOND = now.second
    
    secondDegres = (SECOND / 60) * 360
    minuteDegres = (MINUTE / 60) * 360 + (secondDegres / 60)
    hourDegres = (HOUR / 12) * 360 + (minuteDegres / 12)
    
    turtle.pencolor("BLACK")
    turtle.pensize(10)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.setheading(90 - hourDegres)
    turtle.pendown()
    turtle.forward(150)  
    turtle.penup()
    turtle.goto(0, 0)

    turtle.pensize(5)
    turtle.setheading(90 - minuteDegres)
    turtle.pendown()
    turtle.forward(200)  
    turtle.penup()
    turtle.goto(0, 0)

    turtle.pencolor("RED")
    turtle.pensize(2)
    turtle.setheading(90 - secondDegres)
    turtle.pendown()
    turtle.forward(300) 
    turtle.penup()
    turtle.goto(0, 0)

    turtle.update() 
    turtle.delay(1000)  