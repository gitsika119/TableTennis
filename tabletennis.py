'''
basic game of table tennis using turtle module
racquet1 => player b, up down arrow keys
racquet2 => player a, w s arrow keys
'''

import turtle
import time
import winsound

score1=0
score2=0

table=turtle.Screen()
table.title("table tennis")
table.bgcolor("blue")
table.setup(width=800,height=600)
table.tracer(0)

racquet1=turtle.Turtle()
racquet1.speed(0)
racquet1.shape("square")
racquet1.color("red")
racquet1.penup()
racquet1.goto(350,0)
racquet1.shapesize(stretch_wid=4,stretch_len=1)

racquet2=turtle.Turtle()
racquet2.speed(0)
racquet2.shape("square")
racquet2.color("red")
racquet2.penup()
racquet2.goto(-350,0)
racquet2.shapesize(stretch_wid=4,stretch_len=1)

ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.x=0.5
ball.y=0.5

def r1up():
    y=racquet1.ycor()
    y+=20
    racquet1.sety(y)
def r1down():
    y=racquet1.ycor()
    y-=20
    racquet1.sety(y)
    
table.listen()
table.onkeypress(r1up, "Up")
table.listen()
table.onkeypress(r1down, "Down")

def r2up():
    y=racquet2.ycor()
    y+=20
    racquet2.sety(y)
def r2down():
    y=racquet2.ycor()
    y-=20
    racquet2.sety(y)
    
table.listen()
table.onkeypress(r2up, "w")
table.listen()
table.onkeypress(r2down, "s")

pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0\t\t\tPlayer B: 0",align="center",font=("Calibri",15, "normal"))
time.sleep(1)

while True:
    table.update()
    ball.setx(ball.xcor() + ball.x)
    ball.sety(ball.ycor() + ball.y)
    
    if ball.ycor()>290:
        ball.sety(290)
        ball.y*=-1
        winsound.PlaySound("hit.wav",winsound.SND_ASYNC)
        
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.y*=-1
        winsound.PlaySound("hit.wav",winsound.SND_ASYNC)

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.x*=-1
        score1+=1
        pen.clear()
        pen.write("Player A: {}\t\t\tPlayer B: {}".format(score1,score2),align="center",font=("Calibri",15, "normal"))   
        winsound.PlaySound("point.wav",winsound.SND_ASYNC)
        time.sleep(2)

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.x*=-1
        score2+=1
        pen.clear()
        pen.write("Player A: {}\t\t\tPlayer B: {}".format(score1,score2),align="center",font=("Calibri",15, "normal"))
        winsound.PlaySound("point.wav",winsound.SND_ASYNC)
        time.sleep(2)

    if ball.xcor()>330 and (ball.ycor()<racquet1.ycor()+50 and ball.ycor()>racquet1.ycor()-50) and ball.xcor()>330:
        ball.setx(330)
        ball.x*=-1
        winsound.PlaySound("hit.wav",winsound.SND_ASYNC)

    if ball.xcor()<-330 and (ball.ycor()<racquet2.ycor()+50 and ball.ycor()>racquet2.ycor()-50) and ball.xcor()<-330:
        ball.setx(-330)
        ball.x*=-1 
        winsound.PlaySound("hit.wav",winsound.SND_ASYNC)
        