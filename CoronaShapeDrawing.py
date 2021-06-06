# This Code is Given By Coder Mohit.
# Follow me On Instagram, Facebook.
# Subscribe Coder Mohit YouTube Channel.
# Website Codermohit.com
import turtle
CODERMOHIT = turtle.Turtle()
coderMohit =turtle.Screen()
turtle.screensize(1400,1400)
coderMohit.bgcolor("black")
CODERMOHIT.pencolor("dark green")
CODERMOHIT.pensize(2)
var1=0
var2=0
CODERMOHIT.speed(0)
CODERMOHIT.penup()
CODERMOHIT.goto(0,256)
CODERMOHIT.pendown()
while True:
    CODERMOHIT.forward(var1)
    CODERMOHIT.right(var2)
    var1+=3
    var2+=1
    if var2==210:
        break
    CODERMOHIT.hideturtle()
CODERMOHIT.pencolor('red')
CODERMOHIT.write("Stay Home Stay Safe\n By Coder Mohit",'false', 'center', font=('Showcard gothic', 40))
turtle.done()