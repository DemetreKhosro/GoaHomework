from turtle import begin_fill, color, end_fill, exitonclick, forward, goto, left, pendown, penup, right, speed, width

#we want to paint a house
#step 1: draw a square

speed(30)

width(6)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of square


#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)      #height of door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

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

#drawing windows

penup()
forward(40)
right(240)
forward(40)
pendown()


width(4)
color("green")
begin_fill()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()


penup()
begin_fill()
right(90)
forward(120)
pendown()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
end_fill()


exitonclick()