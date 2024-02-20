from turtle import *

#we want to paint a house
#step 1: draw a square

width(5)

speed(100)

color("blue")
begin_fill()
forward(200)
left(90) 

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of squear

#drawing a door

forward(75)
left(90)
color("yellow")
begin_fill()
forward(100)
right(90)
forward(55)
right(90)
forward(100)
end_fill()
#end of door

#drawing a hood
penup()
goto(200, 200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of hood

exitonclick()