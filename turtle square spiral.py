import turtle
import random
window=turtle.Screen()
status=turtle.textinput("sawal","Do you want to disco?")

brad=turtle.Turtle()
for i in range(500):
    window.bgcolor(random.randint(50,100)/100.0,random.randint(50,100)/100.0,random.randint(50,100)/100.0)
    brad.pencolor(random.randint(50,100)/100.0,random.randint(50,100)/100.0,random.randint(50,100)/100.0)
    brad.speed("slowest")
    brad.forward(i)
    brad.left(91)
window.bgcolor('black')
turtle.mainloop()
