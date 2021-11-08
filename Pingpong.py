# Ping Pong Game
# First App
# By "Disha Patil"

import turtle as t


playerAscore = 0
playerBscore = 0

window = t.Screen()
window.title('Ping Pong Game')
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer(0)

#creating left paddle
leftPaddle = t.Turtle()
leftPaddle.speed(0)
leftPaddle.shape('square')
leftPaddle.color('white')
leftPaddle.shapesize(stretch_wid=5, stretch_len=1)
leftPaddle.penup()
leftPaddle.goto(-350,0)

# creating right paddle
rightPaddle = t.Turtle()
rightPaddle.speed(0)
rightPaddle.shape('square')
rightPaddle.color('white')
rightPaddle.shapesize(stretch_wid=5, stretch_len=1)
rightPaddle.penup()
rightPaddle.goto(350,0)

# creating ball
ball = t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('yellow')
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = 0.2

# creating pen for scoreboard update
pen = t.Turtle()
pen.speed(0)
pen.color('skyblue')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('score', align='center', font=('Arial', 24, 'normal'))

# moving the left paddle
def leftPaddleUp():
    y=leftPaddle.ycor()
    y+=20
    leftPaddle.sety(y)

def leftPaddleDown():
    y=leftPaddle.ycor()
    y-=20
    leftPaddle.sety(y)

#moving the right paddle
def rightPaddleUp():
    y=rightPaddle.ycor()
    y+=20
    rightPaddle.sety(y)

def rightPaddleDown():
    y=rightPaddle.ycor()
    y-=20
    rightPaddle.sety(y)

# Assign keys to play
window.listen()
window.onkeypress(leftPaddleUp,'w')
window.onkeypress(leftPaddleDown,'s')
window.onkeypress(rightPaddleUp,'Up')
window.onkeypress(rightPaddleDown,'Down')

# Main Game Loop
while True:
    window.update()

    # moving a ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # setting up border
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *= -1
        playerAscore += 1
        pen.clear()
        pen.write('player A:{}   player B:{}'.format(playerAscore,playerBscore),align='center', font=('Arial',24,'normal'))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *= -1
        playerBscore += 1
        pen.clear()
        pen.write('player A:{}   player B:{}'.format(playerAscore,playerBscore),align='center', font=('Arial',24,'normal'))

    # Handling the collision
    if(ball.xcor()>340)and(ball.xcor()<350)and(ball.ycor()<rightPaddle.ycor()+40 and ball.ycor()>rightPaddle.ycor()-40):
        ball.setx(340)
        ball.dx *= -1

    if(ball.xcor()<-340)and(ball.xcor()>-350)and(ball.ycor()<leftPaddle.ycor()+40 and ball.ycor()>leftPaddle.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1
