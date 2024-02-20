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


#drawing fllowers

penup()
goto(300, 0)
pendown()

width(3)
color("green")
speed(69)
right(150)
forward(35)
width(3)
begin_fill()
color("purple")
circle(6)
forward(7)
left(55)
circle(-6)
left(100)
circle(-6)
right(200)
circle(-6)
color("yellow")
end_fill()

penup()
goto(282, 0)
pendown()

left(208)

width(3)
color("green")
speed(69)
right(150)
forward(35)
width(3)
begin_fill()
color("purple")
circle(6)
forward(7)
left(55)
circle(-6)
left(100)
circle(-6)
right(200)
circle(-7)
color("red")
end_fill()
#end of fllowers

#drawing the sun
penup()
goto(35, 280)
pendown()
begin_fill()
color("yellow")
circle(55)
end_fill()

penup()
goto(35000000, 10000000)
pendown()




exitonclick()