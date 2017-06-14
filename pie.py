# draws a pie with a knife cutting it
import turtle
lance = turtle.Turtle()
wn = turtle.Screen()

#background color
wn.bgcolor("dimgray")

#make the crust
def spyro():
    for num in range(72):
        lance.forward(200)
        lance.left(90)
        lance.forward(200)
        lance.left(90)
        lance.forward(200)
        lance.left(90)
        lance.forward(200)
        lance.left(5)

lance.pencolor("gold")
lance.speed(0)
lance.pensize(25)
spyro()

#put the cherry filling
def spyro2():
    for num in range(72):
        lance.forward(180)
        lance.left(90)
        lance.forward(180)
        lance.left(90)
        lance.forward(180)
        lance.left(90)
        lance.forward(180)
        lance.left(5)
        
lance.pencolor("red")
lance.pensize(25)
spyro2()

#cover the filling with more crust
def spyro3():
    for num in range(37):
        lance.forward(180)
        lance.left(90)
        lance.forward(180)
        lance.left(90)
        lance.forward(180)
        lance.left(90)
        lance.forward(180)
        lance.left(5)
        
lance.pencolor("gold")
lance.pensize(20)
spyro3()

#don't forget air holes
def spyro4():
    for num in range(5):
        lance.pencolor("gold")
        lance.backward(15)
        lance.forward(2)
        lance.pencolor("red")
        lance.forward(2)
        lance.pencolor("gold")
        lance.forward(1)
        lance.left(20)
        lance.pencolor("gold")
        lance.forward(2)
        lance.pencolor("red")
        lance.forward(2)
        lance.pencolor("gold")
        lance.forward(1)
        lance.left(20)
        lance.pencolor("gold")
        lance.forward(2)
        lance.pencolor("red")
        lance.forward(2)
        lance.pencolor("gold")
        lance.forward(1)
        lance.left(20)
        lance.pencolor("gold")
        lance.forward(2)
        lance.pencolor("red")
        lance.forward(2)
        lance.pencolor("gold")
        lance.forward(1)
        lance.left(20)
        lance.pencolor("red")
        
lance.pensize(5)
spyro4()
lance.penup()
lance.forward(300)
lance.pencolor("black")
lance.pendown()
lance.backward(200)
