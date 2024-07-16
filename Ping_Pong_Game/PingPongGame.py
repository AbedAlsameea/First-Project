import turtle  # drawing module
wind = turtle.Screen()  # intialize  a screen
wind.title("Ping Pong Game By Abed")  # create the game name
wind.bgcolor("black")  #screen color
wind.setup(width=800, height=600)
wind.tracer(0)  # stop auto screen update = 0
#racket 1
racket1 = turtle.Turtle()  #intialize turtle obj(shape)
racket1.speed(0)  # set the speed of animation
racket1.shape("square") # set the shape of the obj
racket1.color("blue") #set the color of the shape
racket1.shapesize(stretch_wid=5, stretch_len=1) #stretch the shape
racket1.penup() #stops the obj from drawing lines
racket1.goto(-350, 0) # set the position of the obj
#racket 2
racket2 = turtle.Turtle()
racket2.speed(0)
racket2.shape("square")
racket2.color("red")
racket2.shapesize(stretch_wid=5, stretch_len=1)
racket2.penup()
racket2.goto(350, 0)
#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1

#score
score1 =0
score2 =0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player 1 : 0 |  player 2 : 0 " , align="center" , font=("courier",24,"normal"))


#Functions
def racket1_up():
    y = racket1.ycor()
    y +=20
    racket1.sety(y)
def racket1_down():
    y = racket1.ycor()
    y -= 20
    racket1.sety(y)


def racket2_up():
    y = racket2.ycor()
    y +=20
    racket2.sety(y)
def racket2_down():
    y = racket2.ycor()
    y -= 20
    racket2.sety(y)


#keyboard binding
wind.listen()
wind.onkeypress(racket1_up , "w")
wind.onkeypress(racket1_down , "s")
wind.onkeypress(racket2_up , "Up")
wind.onkeypress(racket2_down , "Down")

#  main game loop
while True:
    wind.update() #  update the screen everytime the loop run
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() >290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("Player 1 : {} |  player 2 : {} ".format(score1,score2), align="center", font=("courier", 24, "normal"))

    if ball.xcor() <-390:
        ball.goto(0,0)
        ball.dx *= -1
        score2 += 1
        score.color()
        score.write("Player 1 : {} |  player 2 : {} ".format(score1, score2), align="center",font=("courier", 24, "normal"))

    if racket1.ycor() > 250:
        racket1.sety(250)
    if racket1.ycor() < -250:
        racket1.sety(-250)
    if racket2.ycor() > 250:
        racket2.sety(250)
    if racket2.ycor() < -250:
        racket2.sety(-250)
    if (ball.xcor() > 340 and ball.xcor()<350) and (ball.ycor()< racket2.ycor() +40 and ball.ycor() > racket2.ycor()-40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor()> -350) and (ball.ycor()< racket1.ycor() +40 and ball.ycor() > racket1.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1




