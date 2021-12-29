# PONG GAME
import turtle
import random
import time

random_list_x = [4,-4]
random_list_y = [4,-4]

# setup screen
wn = turtle.Screen()
wn.title("pong game")
wn.bgcolor("purple")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.speed(0)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.speed(0)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)


# ball
ball = turtle.Turtle()
ball.shape("square")
ball.speed(10)
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = random.choice(random_list_x)
ball.dy = random.choice(random_list_y)

# Score
score_a = 0
score_b = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: {score_a:>3}  Player B: {score_b:>3}", align="center", font=("Courier", 24, "normal"))

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)

# game end condition
def highest_score(score_a, score_b):
    if score_a > score_b:
        return "Player A", score_a
    return "Player B", score_b


#keyboard biding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")   
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")  

wn.tracer(1)
# Main game loop
while True:
    wn.update() # To be used when tracer is turned off.

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    
    # top and bottom
    if ball.ycor() > 290:
        ball.dy *= -1


    elif ball.ycor() < -290:
        ball.dy *= -1

    # right and left
    if ball.xcor() > 350:
        ball.hideturtle()
        ball.home()
        ball.showturtle()
        ball.dx = random.choice(random_list_x)
        ball.dy = random.choice(random_list_y)
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a:>3}  Player B: {score_b:>3}", align="center", font=("Courier", 24, "normal"))
        wn.update()
        
    elif ball.xcor() < -350:
        ball.hideturtle()
        ball.home()
        ball.showturtle()
        ball.dx = random.choice(random_list_x)
        ball.dy = random.choice(random_list_y)
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a:>3}  Player B: {score_b:>3}", align="center", font=("Courier", 24, "normal"))
        wn.update()

    # flip direction if ball is on paddle
    if ball.xcor() <= -340 and ball.ycor() <= paddle_a.ycor() + 50 and ball.ycor() >= paddle_a.ycor() - 50:
        ball.dx *= -1 # flip direction first
        ball.dx += 2 

    elif ball.xcor() >= 340 and ball.ycor() <= paddle_b.ycor() + 50 and ball.ycor() >= paddle_b.ycor() - 50:
        ball.dx *= -1
        ball.dx -= 2
        
        
    # reloacating paddles
    if paddle_a.ycor() > 300:
        paddle_a.sety(-300) 
        
    elif paddle_a.ycor() < -300:
        paddle_a.sety(300) 
        
    if paddle_b.ycor() > 300:
        paddle_b.sety(-300) 
        
    elif paddle_b.ycor() < -300:
        paddle_b.sety(300) 
        
    # Game End
    if score_a > 3 or score_b > 3:
        name, result = highest_score(score_a, score_b)
        break

# LAST RESULT AND THE END
pen.goto(0,150)
pen.color("cyan")
pen.write(f"{name} won by {result} points",align="center", font=("Courier", 30, "normal"))

time.sleep(4)
wn.bye()
wn.exitonclick() 